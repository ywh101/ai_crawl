# coding: utf-8

from crawl_picture import download_ps


if __name__=='__main__':
    url = input('Please input the URL:')
    data = download_ps.download_page(url)
    download_ps.get_image(data)
