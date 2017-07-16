# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup as soup
import re
import os
import time


def download_page(url):
    headers = {'user-agent':'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    return data

def get_image(data):
    num = 1

    strs = os.getcwd()
    path_dir = os.path.join(strs, 'pictures')
    if not os.path.isdir(path_dir):
        os.mkdir(path_dir, 0o755)

    contents = soup(data, 'html.parser', from_encoding='utf-8')
    imgs = contents.findAll('img', src=re.compile(r'^(http)'))
    for img in imgs:
        link = img['src']
        if re.compile(r'gif|GIF$').search(link):
            pass
        image = download_page(link)
        if re.compile(r'PNG|png$').search(link):
            pat = 'png'
        elif re.compile(r'JPEG|jpeg$').search(link):
            pat = 'jpeg'
        else:
            pat = 'jpg'
        with open(path_dir+"/%d.%s"%(num, pat), 'wb') as fimg:
            fimg.write(image)
        print('downloading %d pictures'%num)
        num += 1
        time.sleep(1)

