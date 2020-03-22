#!usr/bin/python3
"""
@author:    Jokin
@link:      https://github.com/jokin1999/SMMS_Uploader
"""
# -*- coding: utf-8 -*-

import os
import re
import json
import tkinter as tk
from tkinter import ttk
import requests
import urllib3
import time
import threading

THREAD_GET_RELAY = None
CLOUD_LINK = 'https://smmscloud.srv.twocola.com/'
RELAY = []
UI_CONTROL = {}


class smcloud:

    """
    This class is made for SMMS Uploader
    @author:    Jokin
    """

    @classmethod
    def tips(cls, text, sleep=0, default='就绪'):
        """
        Control the bottom tips label
        """
        global UI_CONTROL

        UI_CONTROL['label_status']['text'] = text

        if sleep != 0:
            # time.sleep(sleep)
            UI_CONTROL['label_status']['text'] = default

    @classmethod
    def notepad(cls, filename):
        print('notepad ' + filename)
        os.system('notepad ' + filename)

    @classmethod
    def change_relay(cls):
        """
        Change relay
        """
        global RELAY

        if not os.path.exists('./save.txt'):
            cls.tips('找不到save.txt')
            return False
        try:
            with open('./save.txt', 'r+', encoding='utf-8') as f:
                data = f.read()
        except Exception:
            cls.tips('读取文件时出错，请检查权限')
        else:
            relay = UI_CONTROL['cbox'].get()
            if (relay == ''):
                cls.tips('无效的中继')
                return False
            pattern = r'[http|https]:\/\/(.+?)\/.+,'
            result = re.findall(pattern, data, re.M)
            if len(result) == 0:
                cls.tips('替换失败')
                return False
            result = list(set(result))
            for res in result:
                data = data.replace(res, RELAY['v1']['prefix'] + relay + RELAY['v1']['suffix'])
            try:
                with open('./save2.txt', 'w+', encoding='utf-8') as f:
                    f.write(data)
            except Exception:
                cls.tips('写出 save2.txt 失败')
            else:
                # thr = threading.Thread(target=cls.notepad, args=['./save2.txt'], daemon=True)
                # thr.start()
                cls.tips('成功')

    @classmethod
    def get_relay(cls):
        global THREAD_GET_RELAY
        if THREAD_GET_RELAY is None:
            print('AUTO_GETTING_RELAY')
            THREAD_GET_RELAY = threading.Thread(target=cls._thread_get_relay, daemon=True)
            THREAD_GET_RELAY.start()

    @classmethod
    def _thread_get_relay(cls):
        """
        Get the relay server list
        @file:  /deploy/v1/domains_relay_v1.json
        """
        global THREAD_GET_RELAY
        global UI_CONTROL

        cls.tips('获取中继中')
        global CLOUD_LINK
        global RELAY
        url = CLOUD_LINK + 'deploy/v1/domains_relay_v1.json'
        try:
            http = requests.get(url, timeout=10, verify=False)
        except Exception:
            cls.tips('Failed to get relay')
        else:
            try:
                data = http.content.decode('utf-8')
            except Exception:
                cls.tips('Failed to decode relay data')
            else:
                try:
                    RELAY = json.loads(data)
                except Exception:
                    print(data)
                    cls.tips('Failed to load relay data')
                else:
                    print(RELAY)
                    UI_CONTROL['cbox']['values'] = RELAY['v1']['list']
                    UI_CONTROL['cbox'].current(0)
                    cls.tips('获取中继成功', 3)
        finally:
            THREAD_GET_RELAY = None

    @classmethod
    def create_ui(cls):
        """
        Initialize user interface
        """
        global UI_CONTROL

        # 主窗口
        win = tk.Toplevel()
        win.title('SMMS Uploader 云服务')
        win.minsize(300, 100)
        win.resizable(False, False)

        cbox = ttk.Combobox(win, width=40, state='readonly')
        cbox.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        UI_CONTROL['cbox'] = cbox

        btn_get_relay = tk.Button(win, text='更新中继列表', command=cls.get_relay)
        btn_get_relay.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5, ipadx=5)

        btn_get_relay = tk.Button(win, text='确认转换', command=cls.change_relay)
        btn_get_relay.grid(row=1, column=2, columnspan=3, sticky=tk.E, padx=5, pady=5, ipadx=5)

        label_status = tk.Label(win, text='准备就绪', fg='#fa6333', anchor=tk.W)
        label_status.grid(row=2, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        UI_CONTROL['label_status'] = label_status

        return win

    @classmethod
    def ui(cls, win):
        """
        Running UI loop
        """
        win.mainloop()

    # @classmethod

    @classmethod
    def __init__(cls):
        """
        Initialize the module
        """
        global THREAD_GET_RELAY
        # 取消关闭验证安全提醒
        urllib3.disable_warnings()
        cls.create_ui()
        cls.get_relay()
        # cls.ui(win)


if __name__ == '__main__':
    print('main')
    smcloud()
