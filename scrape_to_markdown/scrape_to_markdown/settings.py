BOT_NAME = 'scrape_to_markdown'

SPIDER_MODULES = ['scrape_to_markdown.spiders']
NEWSPIDER_MODULE = 'scrape_to_markdown.spiders'

# Disable robots.txt rules
ROBOTSTXT_OBEY = False

# Enable the pipeline
ITEM_PIPELINES = {
    'scrape_to_markdown.pipelines.MarkdownPipeline': 300,
}
