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
