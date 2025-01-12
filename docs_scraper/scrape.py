import requests
from bs4 import BeautifulSoup
import markdownify
from urllib.parse import urljoin
import re

# Function to clean and sanitize text for Markdown
def sanitize_markdown(text):
    return re.sub(r'[\n\r]+', '\n', text).strip()

# Function to scrape a single page
def scrape_page(url):
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the main content (e.g., <main>, <article>, or <body>)
        main_content = soup.find('main') or soup.find('article') or soup.find('body')

        if main_content:
            # Extract the page title (for naming output files)
            page_title = soup.title.text.strip() if soup.title else "Untitled"

            # Extract headers (h1, h2, h3, etc.)
            headers = [header.text.strip() for header in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

            # Extract code blocks and their context
            code_examples = []
            for code in main_content.find_all(['pre', 'code']):
                # Get the code block
                code_text = code.text.strip()

                # Find the nearest preceding paragraph or header for context
                context = ""
                prev_element = code.find_previous(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                if prev_element:
                    context = prev_element.text.strip()

                code_examples.append({
                    'code': code_text,
                    'context': context
                })

            # Extract all paragraphs (for general descriptions)
            paragraphs = [p.text.strip() for p in main_content.find_all('p')]

            # Convert the main content to Markdown
            markdown_content = markdownify.markdownify(str(main_content), heading_style="ATX")

            return {
                'url': url,
                'title': page_title,
                'headers': headers,
                'code_examples': code_examples,
                'paragraphs': paragraphs,
                'markdown': markdown_content
            }
        else:
            print(f"No main content found on {url}")
            return None
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Function to crawl a website and scrape all pages
def crawl_website(base_url, max_pages=50):
    visited_urls = set()
    pages_to_visit = [base_url]
    scraped_data = []

    while pages_to_visit and len(scraped_data) < max_pages:
        url = pages_to_visit.pop(0)
        if url not in visited_urls:
            print(f"Scraping: {url}")
            visited_urls.add(url)

            # Scrape the page
            page_data = scrape_page(url)
            if page_data:
                scraped_data.append(page_data)

            # Find all links on the page and add them to the queue
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                for link in soup.find_all('a', href=True):
                    full_url = urljoin(base_url, link['href'])
                    if base_url in full_url and full_url not in visited_urls:
                        pages_to_visit.append(full_url)
            except Exception as e:
                print(f"Error finding links on {url}: {e}")

    return scraped_data

# Function to export all scraped data to a single Markdown file
def export_to_single_markdown(scraped_data, output_file='combined_output.md'):
    with open(output_file, 'w', encoding='utf-8') as md_file:
        for page in scraped_data:
            md_file.write(f"# {page['title']}\n\n")
            md_file.write(f"**URL:** {page['url']}\n\n")
            md_file.write("## Headers\n")
            md_file.write("\n".join(f"- {header}" for header in page['headers']) + "\n\n")
            md_file.write("## Code Examples\n")
            for example in page['code_examples']:
                md_file.write(f"### Context\n{example['context']}\n\n")
                md_file.write(f"```\n{example['code']}\n```\n\n")
            md_file.write("## Paragraphs\n")
            md_file.write("\n".join(f"- {p}" for p in page['paragraphs']) + "\n\n")
            md_file.write("---\n\n")
    print(f"All scraped data exported to {output_file}")

# Main script
if __name__ == "__main__":
    base_url = "https://docs.firecrawl.dev/introduction"  # Replace with your target documentation URL
    max_pages = 300  # Maximum number of pages to scrape

    # Crawl the website and scrape data
    scraped_data = crawl_website(base_url, max_pages)

    # Export all scraped data to a single Markdown file
    export_to_single_markdown(scraped_data)
