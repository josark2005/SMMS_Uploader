#!usr/bin/python3
# -*- coding: utf-8 -*-

import os
import base64
import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
import tkinter.filedialog
import ico
from scanner import scanner

# 全局变量定义
# 文件选择器返回值
_files = []


# 消息盒子定义
def msgbox(message, title='提示', type='info'):
    if (type == 'info'):
        tk.messagebox.showinfo(title=title, message=message)
    elif (type == 'warning'):
        tk.messagebox.showwarning(title=title, message=message)
    elif (type == 'error'):
        tk.messagebox.showerror(title=title, message=message)


# 文件选择器
def selector(mode=0):
    global _files
    filetypes = [('Image files', '*.png;*.jpg;*.gif')]
    if (mode == 0):
        print('单文件选择')
        files = tk.filedialog.askopenfilename(filetypes=filetypes)
        _files.append(files)
    elif (mode == 1):
        print('多文件选择')
        files = tk.filedialog.askopenfilenames(filetypes=filetypes)
        _files.extend(list(files))
    elif (mode == 2):
        print('文件夹遍历')
        directory = tk.filedialog.askdirectory()
        scan = scanner()
        _files.extend(scan.scan(directory))
        pass
    elif (mode == 3):
        # 单层文件夹
        # _files = tk.filedialog.askopenfilenames()
        pass
    # 去重
    _files = list(set(_files))
    # 美化
    for filename in _files:
        _files[_files.index(filename)] = filename.replace('\\', '/')
    # 显示于列表
    _files.sort()
    lsbox_files.set(_files)


def listboxRenew(Listbox_var, list):
    Listbox_var.set(list)


def listRemove(list, removalList):
    for li in removalList:
        list.remove(li)
    return list


def getListboxValueByList(listbox, list):
    values = []
    for li in list:
        values.append(listbox.get(li))
    return values


def _lsbox_remove():
    global _files
    listboxRenew(lsbox_files, listRemove(_files, getListboxValueByList(lsbox, list(lsbox.curselection()))))
    lsbox.select_clear(0, len(_files)-1)


# 读取已成功上传列表
def readSuccessList():
    if not (os.path.exists('./save.txt')):
        return []
    list = []
    file = open('save.txt', 'r+')
    filelists = file.readlines()
    for filelist in filelists:
        info = filelist.strip().split(sep=',', maxsplit=2)
        info[0] = info[0].replace('\\', '/')
        list.append(tuple(info))
    return list


if __name__ == '__main__':
    # 上传模式定义
    upload_modes = [('单个上传', 0, 'normal'), ('群组上传', 1, 'disable')]
    # 选择模式定义
    selector_modes = [('单文件选择', 0, 'normal'), ('多文件选择', 1, 'normal'), ('文件夹遍历', 2, 'normal'), ('单层文件夹', 3, 'disable')]
    # 创建窗口
    win = tk.Tk()
    win.resizable(width=False, height=False)
    icon = open('./icon.ico', 'wb')
    icon.write(base64.b64decode(ico.ico))
    icon.close()
    win.iconbitmap('./icon.ico')
    os.remove('./icon.ico')

    win.title('SMMS图床上传工具')

    # 读取已上传列表
    sUpload = readSuccessList()

    mainFrame = tk.Frame(win)
    mainFrame.grid()

    # 模式标签框架
    lf_mode = tk.LabelFrame(mainFrame, text='上传模式', fg='blue')
    lf_mode.grid(row=1, column=0, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    # 创建RadioButton
    vUpload = tk.IntVar()
    for mode, num, state in upload_modes:
        rb = tk.Radiobutton(lf_mode, text=mode, variable=vUpload, value=num, state=state)
        rb.pack()
        vUpload.set(0)

    # 其他选项框架
    lf_others = tk.LabelFrame(mainFrame, text='其他选项', fg='blue')
    lf_others.grid(row=0, column=3, rowspan=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    vDR = tk.IntVar()
    vSL = tk.IntVar()
    cb_duplicateRemoval = tk.Checkbutton(lf_others, text='检查上传重复（本地）', variable=vDR, state=tk.DISABLED)
    cb_duplicateRemoval.grid(row=0, column=0, sticky=tk.W+tk.S)
    cb_sizeLimitation = tk.Checkbutton(lf_others, text='过滤大于5M的文件', variable=vSL, state=tk.DISABLED)
    cb_sizeLimitation.grid(row=1, column=0, sticky=tk.W+tk.S)

    # 选择器模式标签框架
    lf_selector_mode = tk.LabelFrame(mainFrame, text='选择器模式', fg='blue')
    lf_selector_mode.grid(row=0, column=0, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    # RadioButton
    vSelector = tk.IntVar()
    for mode, num, state in selector_modes:
        rb = tk.Radiobutton(lf_selector_mode, text=mode, variable=vSelector, value=num, state=state)
        rb.pack()
        # 默认多文件选择
        vSelector.set(1)

    # 操作区
    lf_operator = tk.LabelFrame(mainFrame, text='操作区', fg='blue')
    lf_operator.grid(row=0, rowspan=2, column=1, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    # RadioButton
    btn_selector = tk.Button(lf_operator, text='选择', command=lambda: selector(vSelector.get()), width=10)
    btn_selector.grid(padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    btn_upload = tk.Button(lf_operator, text='上传', width=10)
    btn_upload.grid(padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)

    # 已选文件列表
    lf_lsbox = tk.LabelFrame(mainFrame, text='等待上传文件列表', fg='red')
    lf_lsbox.grid(row=0, rowspan=2, column=2, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    lsbox_files = tk.StringVar()
    lsbox = tk.Listbox(lf_lsbox, selectmode=tk.EXTENDED, listvariable=lsbox_files, width=75, relief=tk.FLAT)
    lsbox.grid(row=0, column=0)
    # 右键菜单
    lsbx_rbmenu = tk.Menu(lsbox, tearoff=False)
    lsbx_rbmenu.add_command(label='删除', command=_lsbox_remove)
    # 事件绑定
    lsbox.bind('<Button-3>', func=lambda event: lsbx_rbmenu.post(event.x_root, event.y_root))
    # 滚动条
    lsbox_yscrollbar = tk.Scrollbar(lf_lsbox, command=lsbox.yview)
    lsbox_yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    lsbox.config(yscrollcommand=lsbox_yscrollbar.set)
    lsbox_xscrollbar = tk.Scrollbar(lf_lsbox, command=lsbox.xview, orient='horizontal')
    lsbox_xscrollbar.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    lsbox.config(xscrollcommand=lsbox_xscrollbar.set)

    # 已上传文件列表
    lf_treeview = tk.LabelFrame(mainFrame, text='已上传文件列表（右键复制）', fg='green')
    lf_treeview.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
    # lsbox2_files = tk.StringVar()
    # sUploadList = []
    # for sup in sUpload:
    #     sUploadList.append(sup[0])
    # lsbox2_files.set(sUploadList)
    # lsbox2 = tk.Listbox(lf_lsbox2, selectmode=tk.BROWSE, listvariable=lsbox2_files, width=100, relief=tk.FLAT)
    # lsbox2.grid(sticky=tk.N+tk.S+tk.E+tk.W)
    # # 滚动条
    # lsbox2_yscrollbar = tk.Scrollbar(lf_lsbox2, command=lsbox2.yview)
    # lsbox2_yscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
    # lsbox2.config(yscrollcommand=lsbox2_yscrollbar.set)
    # lsbox2_xscrollbar = tk.Scrollbar(lf_lsbox2, command=lsbox2.xview, orient='horizontal')
    # lsbox2_xscrollbar.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    # lsbox2.config(xscrollcommand=lsbox2_xscrollbar.set)
    treeview = tk.ttk.Treeview(lf_treeview, columns=['path', 'cdn', 'delete'], show='headings', height=10)
    treeview.grid(sticky=tk.N+tk.S+tk.E+tk.W)
    treeview.column('path', width=550, anchor='w')
    treeview.column('cdn', width=200, anchor='w')
    treeview.column('delete', width=200, anchor='w')
    treeview.heading('path', text='本地路径')
    treeview.heading('cdn', text='CDN链接')
    treeview.heading('delete', text='删除链接')
    for sup in sUpload:
        id = treeview.insert('', sUpload.index(sup), value=sup)

    # Footer
    label_bottom = tk.Label(mainFrame, text='Made by Joe', fg='#878787')
    label_bottom_info = '作者：Joe\n鸣谢：SM.MS图床\n本程序开源免费，若有不良商家售卖，给差评！'
    label_bottom.bind('<Double-Button-1>', lambda t: msgbox(label_bottom_info))
    label_bottom.grid(row=3, columnspan=4)

    # 循环
    tk.mainloop()
