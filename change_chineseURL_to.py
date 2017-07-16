# coding: utf-8

from urllib.parse import quote

url = 'http://baike.baidu.com/item/%E6%9D%A8%E7%B4%AB?fr=aladdin'

print(quote(url, safe='/:?='))

