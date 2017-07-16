# coding: utf-8

import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup as soup
import re
import chardet
import os



class htmlDownloader(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        self.bad_urls = set()

    def downloader(self, url, filename):
        #初始化
        headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
        cj = http.cookiejar.CookieJar()

        #预备处理，并读取网页
        req = urllib.request.Request(url, headers=headers)
        handler = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(handler)

        #处理网页编码格式
        resp = opener.open(req).read()
        my_char = chardet.detect(resp)
        code_ma = my_char['encoding']
        print(code_ma)

        #soup网页
        contents = soup(resp, 'html.parser', from_encoding='utf-8')

        #设置路径
        path = os.getcwd()
        path = os.path.join(path, 'text')
        if not os.path.isdir(path):
            os.mkdir(path, 0o755)

        #抓取所需内容，并写入文件
        with open(path+"/%s"%filename, 'a') as f:
            try:
                gets = contents.find('div', {'class':'content_z'}).find_all('p', {'style':'text-indent:2em;'})
                for get in gets:
                    if get.string is not None:
                        f.writelines(get.string+'\n')
                print('Writing is OK!')
                f.write('\n'+'\n'+'++++++++++++++++++++++++++++++++++'+'\n'+'\n'+'\n')
            except Exception as e:
                print(e)
            f.close()

        try:
            #收集新URL
            #出现UnicodeEncodeError，因为部分url中含有中文，无法解析（self._output(request.encode('ascii'))）
            links = contents.find_all('a', href=re.compile(r'^http://'), string=re.compile(r'AI|人工智能'))
            for link in links:
                if re.compile(u'[\u4e00-\u9fa5]+').search(link['href']):
                    self.bad_urls.add(link['href'])
                else:
                    if link['href'] not in self.old_urls:
                        self.new_urls.add(link['href'])
            #print(self.new_urls)
            # print(self.bad_urls)
        except Exception as e:
            print(e)

    #抽取一个新URL，以待爬取
    def get_a_url(self):
        if self.new_urls:
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None


