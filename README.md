# Web Scraping Tools

This repository contains three powerful web scraping tools, each designed for different use cases:

## Tools Overview

| Feature | js_scrape | scrape_to_markdown | github_rag_scraper |
|---------|-----------|---------------------|--------------------|
| Language | JavaScript | Python | Python |
| Command | `node js_scrape/scraper.js domain.xyz/site` | `scrape_to_markdown/run_scrape domain.xyz/site` | `python scrape_github/scripts/github_rag_scraper.py github.com/repo` |
| Output Format | Markdown | Markdown | Structured Data |
| Dependencies | Node.js | Scrapy | Python |
| Best For | General web scraping | Content extraction | GitHub repository data |

## js_scrape

A Node.js based web scraper for extracting structured data from websites.

### Usage
```bash
node js_scrape/scraper.js https://example.com
```

### Features
- Lightweight JavaScript implementation
- Extracts page content into Markdown format
- Easy to modify and extend
- Handles basic web scraping tasks efficiently
- Outputs to `js_scrape/scraped_output/` directory

### Configuration
- Output directory: `js_scrape/scraped_output/`
- Output files are in Markdown format
- Scraped data is excluded from version control (see .gitignore)

## scrape_to_markdown

A Python-based Scrapy project for converting web content into Markdown format.

### Usage
```bash
./scrape_to_markdown/run_scrape https://example.com
```

### Features
- Built on Scrapy framework
- Extracts and converts web content to clean Markdown
- Customizable scraping rules
- Handles complex HTML structures

## github_rag_scraper

A Python tool for extracting and processing GitHub repository data.

### Usage
```bash
python scrape_github/scripts/github_rag_scraper.py https://github.com/user/repo
```

### Features
- Specialized for GitHub repositories
- Extracts repository metadata and content
- Processes data for RAG (Retrieval-Augmented Generation) systems
- Handles GitHub API rate limits

## Installation

### js_scrape
1. Navigate to `js_scrape` directory
2. Run `npm install`

### scrape_to_markdown
1. Navigate to `scrape_to_markdown` directory
2. Run `pip install -r requirements.txt`

### github_rag_scraper
1. Navigate to `scrape_github` directory
2. Run `pip install -r requirements.txt`

## Contribution
Contributions are welcome! Please create an issue or pull request for any improvements or bug fixes.
