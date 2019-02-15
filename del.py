#!usr/bin/python3
# -*- coding: utf-8 -*-

import ssl
import json
import urllib3
ssl._create_default_https_context = ssl._create_unverified_context
urllib3.disable_warnings()


def v1():
    file = open('save.json', 'r+')
    file = file.read()
    filelist = json.loads(file)
    delurls = []
    for data in filelist:
        delurls.append(data['data']['delete'])
    print(delurls)
    count = len(delurls)
    http = urllib3.PoolManager()
    now = 0
    for url in delurls:
        now = now + 1
        print(str(now) + '/' + str(count))
        r = http.request('GET', url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) WallpaperBackuper/1.0.0'})
        if (not r.find('File delete success.') == -1 or not r.find('File already deleted.') == -1):
            print(str(now) + '/' + str(count) + '删除成功！')


def v2():
    file = open('save.txt', 'r+', encoding='utf-8')
    filelist = file.readlines()
    delurls = []
    for line in filelist:
        delurls.append(line.strip().split(sep=',', maxsplit=2)[-1])
    print(delurls)
    count = len(delurls)
    http = urllib3.PoolManager()
    now = 0
    for url in delurls:
        now = now + 1
        r = http.request('GET', url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) WallpaperBackuper/1.0.0'})
        r = r.data.decode()
        if (not r.find('File delete success.') == -1 or not r.find('File already deleted.') == -1):
            print(str(now) + '/' + str(count) + '删除成功！')


if __name__ == '__main__':
    v2()
