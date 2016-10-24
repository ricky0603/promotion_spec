# -*- coding:utf-8 -*-
#@author liaow
import xlrd
from bs4 import BeautifulSoup

excel_source = BeautifulSoup(open('/Users/oraLiao/projects/promotion_spec/config.xml'),'lxml').excelsource.string

class getPrdData:
    
    prd_sheet = xlrd.open_workbook(excel_source)
    prd_info = prd_sheet.sheets()[0]

    def getTitle(self):
        title = self.prd_info.col_values(1)
        return title

    def getUrl(self):
        url = self.prd_info.col_values(2)
        return url
    
    def getPicurl(self):
        pic_url = self.prd_info.col_values(3)
        return pic_url

    def getPriceold(self):
        price_old = self.prd_info.col_values(4)
        return price_old
        
    def getPricecur(self):
        price_cur = self.prd_info.col_values(5)
        return price_cur

    def getTrace(self):
        trace = self.prd_info.col_values(8)[1]
        return trace