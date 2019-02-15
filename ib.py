#!usr/bin/python3
# -*- coding: utf-8 -*-

import os
import smms
import scanner

scan = scanner.scanner()
files = scan.scan('E:\\Wallpapers', ['.jpg', '.png'])
count = len(files)
print('共有' + str(count) + '张图片等待上传')
print(files)
now = 0
# 初始化uploader
uploader = smms.smms()
for tname in files:
    now = now + 1
    print('当前进度： ' + str(now) + '/' + str(count))
    basetname = os.path.basename(tname)
    print(tname + '-->' + os.path.basename(tname))
    file = open(tname, 'rb')
    file_data = file.read()
    file.close()
    r = uploader.post(basetname, file_data)
    r = uploader.parseJson(r)
    if (r['code'] == 'success' and 'msg' not in r):
        # 本地路径-在线地址-删除地址
        file = open('save.txt', 'a', newline='\n', encoding='utf-8')
        file.write(tname + ',' + r['data']['url'] + ',' + r['data']['delete'] + '\n')
        file.close()
        file = open('links.txt', 'a', newline='\n', encoding='utf-8')
        file.write(r['data']['url'])
        file.close()
    else:
        # 失败文件- 失败原因
        file = open('fail.txt', 'a', newline='\n', encoding='utf-8')
        file.write(tname + ',' + r['msg'])
        file.close()
