#-*- coding:utf-8 -*-
#@author liaow
from bs4 import BeautifulSoup
import urllib2

class getPicUrl:
    list = ['33012457']
    path_type = {
    1:"/infosupply/",
    2:"/gifts/",
    3:'/try/'
}
    pic_url = ""
    def getPicUrl(self,prd_id,type):
        for i in self.list:
            url = "http://www.biomart.cn" + self.path_type[type] + str(prd_id) + ".htm"
            response = urllib2.urlopen(url)
            html = BeautifulSoup(response.read(),'lxml')
            pic_url = html.find('div','product_img').img['src']
        return pic_url
print getPicUrl().getPicUrl('33012457',1)