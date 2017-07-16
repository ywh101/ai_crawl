# coding: utf-8

from crawl import search_html
from crawl import email_to
import time


if __name__=='__main__':

    root_url = input('Please input the URL:')
    download = search_html.htmlDownloader()
    email = email_to.email_To()
    filename = input('Please input your filename to write:')
    count = 0

    # 开始，并抓取新URL
    new_url = root_url
    while new_url is not None:
        try:
            start_time = time.time()
            download.downloader(new_url, filename=filename)
            time.sleep(3)
            end_time = time.time()
            print(end_time-start_time)
        except:
            pass
        finally:
            new_url = download.get_a_url()
            count += 1
            print(count)
            if count >= 10:
                break
    email.emailto(filename)
