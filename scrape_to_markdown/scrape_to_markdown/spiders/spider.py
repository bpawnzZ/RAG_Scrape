import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
import markdownify
from urllib.parse import urlparse
import logging

class DomainSpider(CrawlSpider):
    name = 'domain_spider'
    visited_urls = set()
    
    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not start_url:
            raise ValueError("start_url parameter is required")
            
        self.start_urls = [start_url]
        parsed_url = urlparse(start_url)
        self.allowed_domains = [parsed_url.netloc]

    rules = (
        Rule(LinkExtractor(
            allow=(r'.*docs\.litellm\.ai.*',),
            deny_extensions=['pdf', 'jpg', 'png', 'gif', 'zip', 'exe', 'mp3', 'mp4'],
            restrict_xpaths=['//nav', '//main', '//article'],
            tags=['a', 'area'],
            attrs=['href'],
            canonicalize=True,
            unique=True
        ), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # Skip if URL already visited
        if response.url in self.visited_urls:
            self.logger.debug(f"Skipping duplicate URL: {response.url}")
            return
            
        self.visited_urls.add(response.url)
        self.logger.info(f"Processing URL: {response.url}")
        
        try:
            # Extract the title and content of the page
            title = response.css('title::text').get()
            html_content = response.css('body').get()

            if not html_content:
                self.logger.warning(f"No content found at {response.url}")
                return

            # Clean up the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Remove unwanted elements
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'iframe', 'form']):
                element.decompose()

            # Convert the cleaned HTML to Markdown
            cleaned_html = str(soup)
            markdown_content = markdownify.markdownify(cleaned_html, heading_style="ATX")

            if not markdown_content:
                self.logger.warning(f"Empty markdown content at {response.url}")
                return

            # Create and yield the item
            item = {
                'url': response.url,
                'title': title,
                'content': markdown_content
            }
            
            self.logger.info(f"Successfully processed: {response.url}")
            yield item

        except Exception as e:
            self.logger.error(f"Error processing {response.url}: {str(e)}")
            yield {
                'url': response.url,
                'error': str(e)
            }

    def handle_error(self, failure):
        self.logger.error(f"Request failed: {failure.request.url}")
        # Retry logic is handled by Scrapy's retry middleware
