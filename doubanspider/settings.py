# Scrapy settings for doubanspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'doubanspider'

SPIDER_MODULES = ['doubanspider.spiders']
NEWSPIDER_MODULE = 'doubanspider.spiders'
ITEM_PIPELINES = {
    'doubanspider.pipelines.DoubanspiderPipeline': 300
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanspider (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = False
