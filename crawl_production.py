# coding: utf8

import requests
import json
import os
import pandas as pd


URL = 'http://gs.amac.org.cn/amac-infodisc/api/pof/fund?rand=%f&page=%d&size=%d'

header = {
    'Host': 'gs.amac.org.cn',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'http://gs.amac.org.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}

post_data = "{}"

DEFAULT_SIZE = 1000
RANDOM = pd.np.random.random()

OUTPUT_PATH = './output/production'
FILE_NAME = os.path.join(OUTPUT_PATH, 'page%d.csv')
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)


def crawl_1page(page, size=DEFAULT_SIZE):
    url = URL % (RANDOM, page, size)
    response = requests.post(url=url, data=post_data, headers=header)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return False


def extract_data(data):
    num = data['number']
    df = pd.DataFrame(data['content'])
    df.to_csv(FILE_NAME % num, encoding='utf8', index=None)


def crawl():
    data = crawl_1page(0)
    if data is not False:
        is_last = data['last']
        if is_last is True:
            extract_data(data)
        else:
            total_pages = data['totalPages']
            for page in range(0, total_pages):
                print 'downloading...', page, total_pages
                data = crawl_1page(page)
                extract_data(data)
                is_last = data['last']
                if is_last is True:
                    break
            merge_data(total_pages)


def merge_data(total_pages):
    data = pd.DataFrame()
    for page in range(0, total_pages):
        print 'read', page
        temp = pd.read_csv(FILE_NAME % page, encoding='utf8')
        data = pd.concat([data, temp], axis=0, join='outer', ignore_index=True)
    data.to_csv('./output/production.csv', encoding='utf8', index=None)


if __name__ == '__main__':
    # print crawl_1page(0)
    crawl()
    # merge_data(37)
