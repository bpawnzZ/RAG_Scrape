import os
import requests
import argparse
from pathlib import Path

# GitHub API endpoint for repository contents
GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/contents/{path}"

# Function to download a file and append its content to a markdown file
def download_and_append_to_md(url, output_md):
    file_name = url.split('/')[-1]
    
    # Skip .ttf files
    if file_name.endswith('.ttf'):
        print(f"Skipping .ttf file: {file_name}")
        return
    
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        
        # Append the file content to the markdown file
        with open(output_md, 'a') as md_file:
            md_file.write(f"## File: {file_name}\n\n")
            md_file.write("```\n")
            md_file.write(content)
            md_file.write("\n```\n\n")
        print(f"Appended: {file_name}")
    else:
        print(f"Failed to download file: {url}")

# Function to fetch repository contents
def fetch_repo_contents(owner, repo, output_md, token=None, path=""):
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Construct the API URL for the current path
    url = GITHUB_API_URL.format(owner=owner, repo=repo, path=path)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            if item['type'] == 'file':
                # Download and append the file content to the markdown file
                download_and_append_to_md(item['download_url'], output_md)
            elif item['type'] == 'dir':
                # Recursively fetch contents of the directory
                fetch_repo_contents(owner, repo, output_md, token, item['path'])
    else:
        print(f"Failed to fetch repository contents: {response.status_code}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Scrape a GitHub repository and consolidate its contents into a single markdown file.")
    parser.add_argument("url", help="GitHub repository URL")
    parser.add_argument("--token", help="GitHub token for higher rate limits", default=None)
    args = parser.parse_args()

    # Extract owner and repo from URL
    parts = args.url.strip('/').split('/')
    owner = parts[-2]
    repo = parts[-1]

    # Create output directory
    output_dir = os.path.join("repos", owner, repo)
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Create the output markdown file
    output_md = os.path.join(output_dir, f"{repo}_contents.md")
    with open(output_md, 'w') as md_file:
        md_file.write(f"# Repository: {owner}/{repo}\n\n")

    # Fetch repository contents and append to the markdown file
    fetch_repo_contents(owner, repo, output_md, args.token)

    print(f"All contents have been consolidated into: {output_md}")

if __name__ == "__main__":
    main() 
