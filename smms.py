#!usr/bin/python3
# -*- coding: utf-8 -*-

import ssl
import json
import base64
import urllib3


class smms:

    def __init__(self):
        print('SMMS上传类初始化')
        # 关闭证书验证
        ssl._create_default_https_context = ssl._create_unverified_context
        # 取消关闭验证安全提醒
        urllib3.disable_warnings()

    def post(self, filename, file_data, ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) WallpaperBackuper/1.0.0'):
        print('posting: ' + filename)
        filename = str(base64.b64encode(filename.encode('utf-8')), 'utf-8')
        http = urllib3.PoolManager()
        try:
            r = http.request(
                'POST',
                'https://sm.ms/api/upload',
                headers={'user-agent': ua},
                fields={
                    'smfile': (filename, file_data),
                })
        except Exception:
            r = {'code': 'error', 'msg': 'Connection failed.'}
        return r

    def parseJson(self, r):
        try:
            data = r.data.decode('utf-8')
        except Exception:
            data = str(r)
        print(data)
        if (data.find('Request Entity Too Large') != -1):
            return {'code': 'error', 'msg': 'Request Entity Too Large.'}
        else:
            try:
                res = json.loads(data)
            except Exception:
                res = {'code': 'error', 'msg': 'Bad Json Data.'}
            return res


def test():
    file = open('t.png', 'rb')
    file_data = file.read()
    file.close()
    uploader = smms()
    r = uploader.post('t.png', file_data)
    print(uploader.parseJson(r))


if __name__ == '__main__':
    test()
