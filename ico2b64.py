#!usr/bin/python3
# -*- coding: utf-8 -*-


import base64


def a():
    file = open('icon.ico', mode='rb')
    icon = base64.b64encode(file.read())
    file.close()
    file = open('icon.txt', mode='wb')
    file.write(icon)
    file.close()


def b():
    file = open('icon.txt', mode='r+')
    icon = base64.b64decode(file.read())
    file.close()
    file = open('icon2.ico', mode='wb')
    file.write(icon)
    file.close()


if __name__ == '__main__':
    b()
