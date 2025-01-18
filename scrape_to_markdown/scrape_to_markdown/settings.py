BOT_NAME = 'scrape_to_markdown'

SPIDER_MODULES = ['scrape_to_markdown.spiders']
NEWSPIDER_MODULE = 'scrape_to_markdown.spiders'

# Disable robots.txt rules
ROBOTSTXT_OBEY = False

# Enable the pipeline
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'scrape_to_markdown.pipelines.MarkdownPipeline': 300,
}

# Configure image pipeline
IMAGES_STORE = 'images'
IMAGES_URLS_FIELD = 'image_urls'
IMAGES_RESULT_FIELD = 'images'
IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}

# Configure retry middleware
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429]
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Configure duplicate prevention
DUPEFILTER_CLASS = 'scrapy.dupefilters.RFPDupeFilter'
DUPEFILTER_DEBUG = True

# Configure request throttling
DOWNLOAD_DELAY = 2.0
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# Configure user-agent rotation
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
ROTATING_PROXY_LIST = [
    # Add proxy list here if needed
]

# Configure caching
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 60 * 60 * 24  # 1 day
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [500, 502, 503, 504, 408, 429]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Configure logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
