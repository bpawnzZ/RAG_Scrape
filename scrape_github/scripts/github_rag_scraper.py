import os
import sys
import re
import git
from pathlib import Path
from typing import List, Dict

def clone_repo(repo_url: str, target_dir: Path) -> Path:
    """Clone repository and return path to cloned directory"""
    try:
        print(f"Cloning repository: {repo_url}")
        repo_dir = target_dir / repo_url.split('/')[-1].replace('.git', '')
        git.Repo.clone_from(repo_url, repo_dir)
        return repo_dir
    except Exception as e:
        print(f"Error cloning repository: {e}")
        sys.exit(1)

def process_file(file_path: Path) -> str:
    """Process individual file content for RAG optimization"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic RAG optimization
        content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
        content = re.sub(r'[^\x00-\x7F]+', ' ', content)  # Remove non-ASCII
        content = content.strip()
        
        return f"# File: {file_path.relative_to(file_path.parent.parent)}\n\n{content}\n\n"
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return ""

def process_repo(repo_dir: Path) -> str:
    """Process all files in repository"""
    md_content = f"# Repository: {repo_dir.name}\n\n"
    
    # Process files in order of importance
    priority_files = ['README.md', 'LICENSE', '*.py', '*.md', '*.txt']
    processed_files = set()
    
    for pattern in priority_files:
        for file_path in repo_dir.rglob(pattern):
            if file_path.is_file() and file_path not in processed_files:
                md_content += process_file(file_path)
                processed_files.add(file_path)
    
    # Process remaining files
    for file_path in repo_dir.rglob('*'):
        if file_path.is_file() and file_path not in processed_files:
            md_content += process_file(file_path)
            processed_files.add(file_path)
    
    return md_content

def save_md(content: str, repo_name: str, output_dir: Path) -> Path:
    """Save processed content to markdown file"""
    output_path = output_dir / f"{repo_name}_contents.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return output_path

def cleanup(repo_dir: Path):
    """Remove cloned repository"""
    try:
        print(f"Cleaning up: {repo_dir}")
        os.system(f"rm -rf {repo_dir}")
    except Exception as e:
        print(f"Error during cleanup: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python github_rag_scraper.py <repository_url>")
        sys.exit(1)
    
    repo_url = sys.argv[1]
    repos_dir = Path("repos")
    repos_dir.mkdir(exist_ok=True)
    
    # Clone repository
    repo_dir = clone_repo(repo_url, repos_dir)
    
    # Process repository
    md_content = process_repo(repo_dir)
    
    # Save markdown
    output_path = save_md(md_content, repo_dir.name, repos_dir)
    print(f"Saved processed content to: {output_path}")
    
    # Cleanup
    cleanup(repo_dir)

if __name__ == "__main__":
    main()