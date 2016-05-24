#!/usr/bin/env python

import logging, re, sys
from scrapy.spider import BaseSpider
from scrapy.http import Request
from BeautifulSoup import BeautifulSoup
from .. import items

#sys.stdout=open('E:\Project\doubanspider\doubanspider\output.txt','w')

class DoubanSpider(BaseSpider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://book.douban.com/"
#        "https://movie.douban.com/"
#        "https://music.douban.com/"
    ]

    pattern = re.compile("https://book.douban.com/subject/\d+")

    def parse(self,response):
        soup = BeautifulSoup(response.body)
        tags = soup.findAll('a',href = self.pattern)
        for tag in tags:
            url = tag.get('href')
            m = re.match(self.pattern,url)
            url = m.group()
            if url is None:
                continue
            print url
            yield Request(url,callback = self.parse_item)

    def parse_item(self,response):
        parser = BookParser()
        item = parser.parse(response.body)
        soup = BeautifulSoup(response.body)
        tags = soup.findAll('a',href = self.pattern)
        for tag in tags:
            url = tag.get('href')
            m = re.match(self.pattern,url)
            url = m.group()
            print url
            yield Request(url,callback = self.parse_item)
        yield item
#        self.parse(response)


class BookParser(object):
    
    def parse(self,html):
        soup = BeautifulSoup(html)
        item = items.BookItem()
        item['name'] = self.getName(soup)
        item['author'] = self.getAuthor(soup)
        item['picture'] = self.getPicture(soup)
        item['grade'] = self.getGrade(soup)
        return item

    def getName(self,soup):
        return soup.find('h1').find('span').string

    def getAuthor(self,soup):
        return soup.find('div',id='info').find('span').find('a').string

    def getPicture(self,soup):
        return soup.find('div',id='mainpic').find('a').find('img').get('src')

    def getGrade(self,soup):
        return soup.find('strong').string
        
        
        
