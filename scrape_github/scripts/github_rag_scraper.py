import os
import sys
import re
import git
import hashlib
from pathlib import Path
from typing import List, Dict, Set

# Extended set of binary file extensions
BINARY_EXTENSIONS = {
    # Image formats
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.svg', '.webp',
    # Audio/video formats
    '.mp3', '.mp4', '.wav', '.avi', '.mov', '.mkv',
    # Executables and libraries
    '.exe', '.dll', '.so', '.bin', '.pyc', '.class',
    # Archives
    '.zip', '.tar', '.gz', '.bz2', '.7z', '.rar',
    # Database files
    '.sqlite', '.db', '.sqlite3', '.mdb',
    # Fonts
    '.ttf', '.otf', '.woff', '.woff2', '.eot',
    # Other binary formats
    '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.suo', '.sln', '.vs', '.dmg', '.iso', '.img',
    # Hidden/system files
    '.DS_Store', '.git', '.svn', '.hg'
}

def clone_repo(repo_url: str, target_dir: Path) -> Path:
    """Clone repository and return path to cloned directory"""
    try:
        print(f"Cloning repository: {repo_url}")
        
        # Verify URL format
        if not re.match(r'^https://github\.com/[^/]+/[^/]+(\.git)?$', repo_url):
            raise ValueError(f"Invalid GitHub repository URL format: {repo_url}")
            
        repo_dir = target_dir / repo_url.split('/')[-1].replace('.git', '')
        
        # Check if we can write to target directory
        if not os.access(target_dir, os.W_OK):
            raise PermissionError(f"Cannot write to directory: {target_dir}")
            
        # Clone with progress
        print("Cloning...")
        repo = git.Repo.clone_from(repo_url, repo_dir, progress=git.remote.RemoteProgress())
        print("Clone successful")
        return repo_dir
    except git.exc.GitCommandError as e:
        print(f"Git command failed: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

def is_binary_file(file_path: Path) -> bool:
    """Check if file is binary based on extension and content"""
    # Check extension
    if file_path.suffix.lower() in {ext.lower() for ext in BINARY_EXTENSIONS}:
        return True
        
    # Check for .git directories
    if '.git' in file_path.parts:
        return True
        
    # Check file content
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\x00' in chunk:  # Null bytes indicate binary
                return True
    except:
        return True
        
    return False

def process_file(file_path: Path, content_hashes: Set[str]) -> str:
    """Process individual file content for RAG optimization"""
    if is_binary_file(file_path):
        return ""
        
    try:
        # Read file with multiple encoding attempts
        encodings = ['utf-8', 'latin-1', 'iso-8859-1']
        content = None
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
                
        if content is None:
            return ""
            
        # Create content hash to detect duplicates
        content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
        if content_hash in content_hashes:
            return ""
        content_hashes.add(content_hash)
        
        # RAG optimization
        content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
        content = re.sub(r'[^\x00-\x7F]+', ' ', content)  # Remove non-ASCII
        content = content.strip()
        
        # Enhanced metadata
        return (f"# File: {file_path.relative_to(file_path.parent.parent)}\n"
                f"## Path: {file_path}\n"
                f"## Size: {os.path.getsize(file_path)} bytes\n\n"
                f"```\n{content}\n```\n\n")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return ""

def process_repo(repo_dir: Path) -> str:
    """Process all files in repository"""
    md_content = f"# Repository: {repo_dir.name}\n\n"
    content_hashes = set()
    
    # Process files in order of importance
    priority_files = ['README.md', 'LICENSE', '*.py', '*.md', '*.txt', '*.js', '*.ts',
                     '*.java', '*.c', '*.cpp', '*.h', '*.html', '*.css', '*.json',
                     '*.yaml', '*.yml', '*.xml']
    
    processed_files = set()
    
    for pattern in priority_files:
        for file_path in repo_dir.rglob(pattern):
            if file_path.is_file() and file_path not in processed_files:
                file_content = process_file(file_path, content_hashes)
                if file_content:
                    md_content += file_content
                    processed_files.add(file_path)
    
    # Process remaining files
    for file_path in repo_dir.rglob('*'):
        if file_path.is_file() and file_path not in processed_files:
            file_content = process_file(file_path, content_hashes)
            if file_content:
                md_content += file_content
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