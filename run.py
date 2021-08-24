import sys
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

"""
-s : for search
-l : for location
"""

search_term = sys.argv[sys.argv.index("-s")+1]
location = sys.argv[sys.argv.index("-l")+1]

link = f'https://www.yelp.com/search?find_desc={search_term}&find_loc={location}'

process = CrawlerProcess(get_project_settings())

process.crawl('yelp', link=link)

process.start()
