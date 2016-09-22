# -*- coding:utf-8 -*-
import xlrd

class getPrdData:

    prd_sheet = xlrd.open_workbook('/Users/oraLiao/projects/promotion_spec/1.xlsx')
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

