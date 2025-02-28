import os
import requests
import argparse
import time
import logging
import configparser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

# Load configuration
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../../config.ini'))

# Supported file extensions
SUPPORTED_EXTENSIONS = {
    '.md', '.txt', '.py', '.js', '.ts', '.java', '.c', '.cpp', '.h',
    '.html', '.css', '.json', '.yaml', '.yml', '.xml', '.csv', '.sh'
}

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# GitHub API endpoint for repository contents
GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}/contents"

# Rate limit handling
def handle_rate_limit(response):
    if response.status_code == 403 and 'X-RateLimit-Remaining' in response.headers:
        if int(response.headers['X-RateLimit-Remaining']) == 0:
            reset_time = int(response.headers['X-RateLimit-Reset'])
            sleep_time = max(reset_time - time.time(), 0) + 1
            logger.warning(f"Rate limit exceeded. Sleeping for {sleep_time:.1f} seconds")
            time.sleep(sleep_time)
            return True
    return False

# Function to download a file
def download_file(url, output_dir, max_retries=3):
    file_name = url.split('/')[-1]
    file_path = os.path.join(output_dir, file_name)
    
    # Skip if file already exists
    if os.path.exists(file_path):
        logger.info(f"Skipping existing file: {file_name}")
        return
        
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                logger.info(f"Downloaded: {file_name}")
                return
            else:
                logger.warning(f"Failed to download {file_name}: HTTP {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt + 1} failed for {file_name}: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
    
    logger.error(f"Failed to download {file_name} after {max_retries} attempts")

# Function to fetch repository contents
def fetch_repo_contents(owner, repo, output_dir, token=None, max_workers=4, max_retries=3):
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = GITHUB_API_URL.format(owner=owner, repo=repo)
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if handle_rate_limit(response):
                continue
                
            if response.status_code == 200:
                contents = response.json()
                
                # Filter and count files
                filtered_contents = [
                    item for item in contents
                    if item['type'] == 'dir' or
                    (item['type'] == 'file' and
                     os.path.splitext(item['name'])[1].lower() in SUPPORTED_EXTENSIONS)
                ]
                
                # Initialize progress bar
                with tqdm(total=len(filtered_contents), desc=f"Downloading {repo}", unit="file") as pbar:
                    # Process files in parallel
                    with ThreadPoolExecutor(max_workers=max_workers) as executor:
                        futures = []
                        for item in filtered_contents:
                            if item['type'] == 'file':
                                futures.append(executor.submit(
                                    download_file,
                                    item['download_url'],
                                    output_dir
                                ))
                            elif item['type'] == 'dir':
                                futures.append(executor.submit(
                                    fetch_repo_contents,
                                    owner,
                                    repo,
                                    os.path.join(output_dir, item['name']),
                                    token,
                                    max_workers,
                                    max_retries
                                ))
                        
                        # Update progress bar as tasks complete
                        for future in as_completed(futures):
                            try:
                                future.result()
                                pbar.update(1)
                            except Exception as e:
                                logger.error(f"Error processing item: {str(e)}")
                                pbar.update(1)
                return
            else:
                logger.error(f"Failed to fetch repository contents: {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error fetching repository contents: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
    
    logger.error(f"Failed to fetch repository contents after {max_retries} attempts")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Scrape a GitHub repository and download its contents.")
    parser.add_argument("url", help="GitHub repository URL")
    parser.add_argument("--token", help="GitHub token for higher rate limits", default=config['github']['token'])
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
