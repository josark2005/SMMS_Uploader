#!usr/bin/python3
# -*- coding: utf-8 -*-

import ssl
import json
import urllib3


class smms:

    def __init__(self):
        print('initializing...')
        # 关闭证书验证
        ssl._create_default_https_context = ssl._create_unverified_context
        # 取消关闭验证安全提醒
        urllib3.disable_warnings()

    def post(self, filename, file_data, ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) WallpaperBackuper/1.0.0'):
        print('posting: ' + filename)
        http = urllib3.PoolManager()
        r = http.request(
            'POST',
            'https://sm.ms/api/upload',
            headers={'user-agent': ua},
            fields={
                'smfile': (filename, file_data),
            })
        return r

    def parseJson(self, r):
        data = r.data.decode()
        print(data)
        return json.loads(data)


def test():
    file = open('t.png', 'rb')
    file_data = file.read()
    file.close()
    uploader = smms()
    r = uploader.post('t.png', file_data)
    print(uploader.parseJson(r))


if __name__ == '__main__':
    test()
