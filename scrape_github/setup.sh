#!/bin/bash

# Create directories
mkdir -p repos
mkdir -p scripts

# Create the Python script
cat << 'EOF' > scripts/github_scraper.py
import os
import requests
import argparse
from pathlib import Path

# GitHub API endpoint for repository contents
GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/contents"

# Function to download a file
def download_file(url, output_dir):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download file: {url}")

# Function to fetch repository contents
def fetch_repo_contents(owner, repo, output_dir, token=None):
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = GITHUB_API_URL.format(owner=owner, repo=repo)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contents = response.json()
        for item in contents:
            if item['type'] == 'file':
                download_file(item['download_url'], output_dir)
            elif item['type'] == 'dir':
                fetch_repo_contents(owner, repo, os.path.join(output_dir, item['name']), token)
    else:
        print(f"Failed to fetch repository contents: {response.status_code}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Scrape a GitHub repository and download its contents.")
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

    # Fetch repository contents
    fetch_repo_contents(owner, repo, output_dir, args.token)

if __name__ == "__main__":
    main()
EOF

# Make the script executable
chmod +x scripts/github_scraper.py

# Install required Python packages
pip install requests

echo "Setup complete. You can now run the scraper using:"
echo "python scripts/github_scraper.py <GITHUB_REPO_URL> [--token YOUR_GITHUB_TOKEN]"
