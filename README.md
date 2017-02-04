# promotion_spec
###从 Excel 中获取数据并且生成活动页面的脚本

####文件功能说明

* getPrdData.py  从制定的Excel中取数据；
* prdItem.py     将Excel中的数据生成HTML片段
* makeSpec.py    将HTML片段组装进页面模板中
* config.xml     配置文件，配置Excel的地址和页面tdk、统计参数等信息
* demo.html      要生成的页面模板
* 1.xlsx         测试用Excel文件、
* getPicUrl.py   获取商品的图片地址（未完成）


####依赖
* python 2.7
* BeautifulSoup
