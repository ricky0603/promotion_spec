# -*- coding:utf-8 -*-
import getPrdData
import prdItem
from bs4 import BeautifulSoup
import HTMLParser

page_info = BeautifulSoup(open('/Users/oraLiao/projects/promotion_spec/config.xml'),'lxml')

#设置页面标题
title = page_info.title.string

#设置页面描述
desc = page_info.desc.string

#设置banner图地址
banner_url = page_info.bannerurl.string

#设置banner背景色
banner_bgr_color = page_info.banner_bgr_color.string

#设置微信分享图片地址
wx_img = page_info.wximg.string

#设置微信分享标题
wx_title = page_info.wxtitle.string

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
