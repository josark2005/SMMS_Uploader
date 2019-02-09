#!usr/bin/python3
# -*- coding: utf-8 -*-

import os


class scanner:
    def scan(self, path, suffix=None):
        path = os.path.abspath(path)
        filelist = []
        # 判断文件夹是否存在
        if not (os.path.isdir(path)):
            print('Directory does not exist.')
            exit(-2)
        for filename in os.listdir(path):
            abspath = path + '/' + filename
            # 判断是否为子文件夹
            if (os.path.isdir(abspath)):
                filelist.extend(self.scan(abspath, suffix))
            else:
                if (suffix is None):
                    filelist.append(abspath)
                else:
                    # 判断后缀
                    realSuffix = os.path.splitext(abspath)[-1]
                    if (isinstance(suffix, str)):
                        if (suffix == realSuffix):
                            filelist.append(abspath)
                        else:
                            continue
                    else:
                        if (realSuffix in suffix):
                            filelist.append(abspath)
                        else:
                            continue
        return filelist


def test():
    scan = scanner()
    r = scan.scan('./', '.py')
    print(r)


if __name__ == '__main__':
    test()
