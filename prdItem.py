# -*- coding:utf-8 -*-
# @author liaow
from bs4 import BeautifulSoup
import getPrdData
import HTMLParser

class prdItem:
    page_info = BeautifulSoup(open('/Users/oraLiao/projects/promotion_spec/config.xml'),'lxml')
    trace = page_info.trace.string
    def makeItem(self):
        htmlParser = HTMLParser.HTMLParser()
        items = BeautifulSoup(open('/Users/oraLiao/projects/promotion_spec/itemHtml.html').read(),'lxml')
        title = getPrdData.getPrdData().getTitle()
        url = getPrdData.getPrdData().getUrl()
        pic_url = getPrdData.getPrdData().getPicurl()
        price_old = getPrdData.getPrdData().getPriceold()
        price_cur = getPrdData.getPrdData().getPricecur()
        # trace = getPrdData.getPrdData().getTrace()

        for i in range(0,len(title)-1):
            items.div.append(str(items.a))
            new_items = BeautifulSoup(htmlParser.unescape(str(items.div).decode('utf-8')),'lxml')
            new_items.div.contents[i]['href'] = url[i+1] + "?trace=" + self.trace
            new_items.div.contents[i].img['src'] = pic_url[i+1]
            new_items.div.contents[i].h3.string = title[i+1]
            new_items.div.contents[i].find('span','price_cur').string = unicode(price_cur[i+1])
            new_items.div.contents[i].find('span','price_old').string = htmlParser.unescape('原价：'.decode('utf-8')) + unicode(price_old[i+1])
            new_items.div.contents[i].find('div','item__button').string = '立即采购'
            items = new_items
            # print new_items.div.contents[i]['href']

        return new_items.div


