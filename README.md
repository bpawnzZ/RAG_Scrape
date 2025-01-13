# RAG Scrape Tools

This repository contains three different web scraping tools for RAG (Retrieval-Augmented Generation) systems:

1. Website Scraper (scrape_to_markdown)
2. GitHub Repository Scraper (scrape_github)
3. JavaScript Puppeteer Scraper (js_scrape)

## 1. Website Scraper (Python)

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
   scrapy crawl domain_spider -a start_url="https://docs.pydantic.dev/latest/"
   ```
   Replace the URL with the website you want to scrape.

### Output
- Scraped content will be saved in markdown format
- Files are organized by domain and path structure

## 2. GitHub Repository Scraper (Python)

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
   python scripts/github_rag_scraper.py https://github.com/ccxt/ccxt.git
   ```
   Replace the repository URL with the GitHub repository you want to scrape.

### Output
- Repository contents will be saved in markdown format
- Files are organized by repository structure

## 3. JavaScript Puppeteer Scraper

Scrapes website content using Puppeteer and saves it as markdown.

### Requirements
- Node.js 16+
- Install dependencies: `npm install` in the js_scrape directory

### Usage
1. Navigate to the js_scrape directory:
   ```bash
   cd js_scrape
   ```

2. Run the scraper:
   ```bash
   node /home/insomnia/scraper_fixed.js "https://docs.ccxt.com/#/?id=user-defined-clientorderid"
   ```
   Replace the URL with the website URL you want to scrape.

### Features
- Crawls up to 300 pages by default
- Follows same-domain links
- Saves output to `scraped_data.md`
- Preserves URL structure in markdown headers
- Handles network errors gracefully

### Output
- Scraped content will be saved in markdown format
- Each page's content is preceded by its URL as a header
- Output saved to `scraped_data.md` in the js_scrape directory

## Notes
- For GitHub scraping, you need to generate a personal access token with `repo` scope
- All tools preserve the original structure of the content
- Scraped content is suitable for RAG systems and knowledge bases
- Be mindful of website terms of service and GitHub API rate limits
- The JavaScript scraper is particularly useful for JavaScript-heavy websites

## Requirements
Each tool has its own requirements:
- Website Scraper: `scrape_to_markdown/requirements.txt`
- GitHub Scraper: `scrape_github/requirements.txt`
- JavaScript Scraper: `js_scrape/package.json`

Install dependencies for each tool in their respective directories using:
- Python tools: `pip install -r requirements.txt`
- JavaScript tool: `npm install`
