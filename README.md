# RAG Scrape Tools

This repository contains two different web scraping tools for RAG (Retrieval-Augmented Generation) systems:

1. Website Scraper (scrape_to_markdown)
2. GitHub Repository Scraper (scrape_github)

## 1. Website Scraper

Scrapes website content and converts it to markdown format.

### Requirements
- Python 3.8+
- Install dependencies: `pip install -r scrape_to_markdown/requirements.txt`

### Usage
1. Navigate to the scrape_to_markdown directory:
   ```bash
   cd scrape_to_markdown
   ```

2. Run the scraper:
   ```bash
   ./run_spider.sh https://example.com
   ```
   Replace `https://example.com` with the website URL you want to scrape.

### Output
- Scraped content will be saved in markdown format
- Files are organized by domain and path structure

## 2. GitHub Repository Scraper

Scrapes GitHub repository contents including code files and documentation.

### Requirements
- Python 3.8+
- GitHub Personal Access Token (with repo access)
- Install dependencies: `pip install -r scrape_github/requirements.txt`

### Usage
1. Navigate to the scrape_github directory:
   ```bash
   cd scrape_github
   ```

2. Run the scraper:
   ```bash
   python scripts/github_scraper.py https://github.com/owner/repo --token YOUR_GITHUB_TOKEN
   ```
   Replace:
   - `https://github.com/owner/repo` with the GitHub repository URL
   - `YOUR_GITHUB_TOKEN` with your personal access token

### Output
- Repository contents will be saved in markdown format
- Files are organized by repository structure

## Notes
- For GitHub scraping, you need to generate a personal access token with `repo` scope
- Both tools preserve the original structure of the content
- Scraped content is suitable for RAG systems and knowledge bases
- Be mindful of website terms of service and GitHub API rate limits

## Requirements
Both tools require Python 3.8+ and have their own requirements files:
- Website Scraper: `scrape_to_markdown/requirements.txt`
- GitHub Scraper: `scrape_github/requirements.txt`

Install dependencies for each tool in their respective directories using:
