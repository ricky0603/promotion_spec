# -*- coding:utf-8 -*-
import getPrdData
import prdItem
from bs4 import BeautifulSoup
import HTMLParser

#设置页面标题
title = "hahahah"
#设置页面描述
desc = "lalalal"
#设置banner图地址
banner_url = "http://res.dxycdn.com/trademd/upload/pic/2016/09/18/B1474186439965hsw4tcngpe.jpg!orgin"
#设置banner背景色
banner_bgr_color = "#000000"
#设置微信分享图片地址
wx_img = "http://res.dxycdn.com/trademd/upload/pic/2016/09/18/B1474186439965hsw4tcngpe.jpg!orgin"
#设置微信分享标题
wx_title = "lalalalla"

htmlParser = HTMLParser.HTMLParser()
html = BeautifulSoup(open('/Users/oraLiao/projects/promotion_spec/demo.html').read(),'lxml')
seciton_lists = prdItem.prdItem().makeItem()
html.find('div','section').append(seciton_lists)
html.title.string = title
html.find('meta',attrs={'name':'description'})['content'] = desc
html.find('div','banner').img['src'] = banner_url
html.find('div','top_wp')['style'] = "background-color:" + banner_bgr_color
html.find('div','top_wp')['data-sharetitle'] = wx_title
html.find('img',id='j_share_img')['src'] = wx_img

print str(html)