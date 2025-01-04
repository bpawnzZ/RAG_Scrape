#!/bin/bash

# Create project directory
mkdir -p scrape_to_markdown/scrape_to_markdown/spiders
cd scrape_to_markdown

# Create necessary files
touch scrape_to_markdown/__init__.py
touch scrape_to_markdown/spiders/__init__.py
touch scrape_to_markdown/spiders/spider.py
touch scrape_to_markdown/pipelines.py
touch scrape_to_markdown/settings.py
touch scrape_to_markdown/items.py
touch requirements.txt
touch run_spider.sh
touch README.md
touch scrapy.cfg

# Add content to requirements.txt
echo "scrapy" >> requirements.txt
echo "beautifulsoup4" >> requirements.txt
echo "markdownify" >> requirements.txt

# Add content to run_spider.sh
echo '#!/bin/bash' >> run_spider.sh
echo 'if [ -z "$1" ]; then' >> run_spider.sh
echo '  echo "Usage: ./run_spider.sh <URL>"' >> run_spider.sh
echo '  exit 1' >> run_spider.sh
echo 'fi' >> run_spider.sh
echo 'URL=$1' >> run_spider.sh
echo 'scrapy crawl domain_spider -a start_url=$URL' >> run_spider.sh

# Make run_spider.sh executable
chmod +x run_spider.sh

# Add content to README.md
echo "# Scrape to Markdown" >> README.md
echo "This project scrapes a given URL, cleans the data, and saves it as a Markdown file." >> README.md

# Add content to spider.py
cat <<EOL > scrape_to_markdown/spiders/spider.py
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import markdownify

class DomainSpider(CrawlSpider):
    name = 'domain_spider'

    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [start_url.split('/')[2]]  # Extract domain from URL

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Extract the title and content of the page
        title = response.css('title::text').get()
        html_content = response.css('body').get()

        # Clean up the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove unwanted elements (e.g., scripts, styles, navbars, footers)
        for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            element.decompose()

        # Convert the cleaned HTML to Markdown
        cleaned_html = str(soup)
        markdown_content = markdownify.markdownify(cleaned_html, heading_style="ATX")

        # Yield the cleaned data as a dictionary
        yield {
            'url': response.url,
            'title': title,
            'content': markdown_content
        }
EOL

# Add content to pipelines.py
cat <<EOL > scrape_to_markdown/pipelines.py
import os

class MarkdownPipeline:
    def open_spider(self, spider):
        self.markdown_file = open('output.md', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.markdown_file.close()

    def process_item(self, item, spider):
        # Write the URL, title, and content to the Markdown file
        self.markdown_file.write(f"# {item['title']}\n\n")
        self.markdown_file.write(f"**URL:** {item['url']}\n\n")
        self.markdown_file.write(f"{item['content']}\n\n")
        self.markdown_file.write("---\n\n")
        return item
EOL

# Add content to settings.py
cat <<EOL > scrape_to_markdown/settings.py
BOT_NAME = 'scrape_to_markdown'

SPIDER_MODULES = ['scrape_to_markdown.spiders']
NEWSPIDER_MODULE = 'scrape_to_markdown.spiders'

# Disable robots.txt rules
ROBOTSTXT_OBEY = False

# Enable the pipeline
ITEM_PIPELINES = {
    'scrape_to_markdown.pipelines.MarkdownPipeline': 300,
}
EOL

# Add content to items.py
cat <<EOL > scrape_to_markdown/items.py
import scrapy

class ScrapeToMarkdownItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
EOL

# Add content to scrapy.cfg
cat <<EOL > scrapy.cfg
[settings]
default = scrape_to_markdown.settings

[deploy]
#url = http://localhost:6800/
project = scrape_to_markdown
EOL

echo "Project setup complete. Run the spider with: ./run_spider.sh <URL>"
