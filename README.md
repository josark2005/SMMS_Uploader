# ![SMMS Uploader](https://i.loli.net/2019/02/15/5c6678567831c.jpg) SMMS Uploader 图床上传工具

![SMMS Uploader GUI](https://i.loli.net/2019/03/18/5c8f6cd24c9dc.jpg)

（界面截图可能与最新版存在细微差别）

## 下载

- [GitHub发布页](https://github.com/jokin1999/SMMS_Uploader/release)

\*线路无本质区别，请自行选择合适的平台下载

## 文件解释

- `gui.py` GUI模块
- `cloud.py` 云服务模块
- `smms.py` 图床上传模块
- `scanner.py` 文件扫描模块
- `ico.py` ICON文件
- `*save.txt` **上传成功文件列表（自动生成）**
- `*fail.txt` **上传失败文件列表（自动生成）**
- `*links.txt` **CDN链接列表（自动生成）**
- `ib.py` 测试文件（非必要文件）
- `del.py` 自动批量删除模块（非必要文件）
- `ico2b64.py` ICON转换模块（非必要文件）
- `build.bat` EXE文件生成批处理文件（非必要文件）

**自动生成的文件可能随版本更新而变动**

## 使用Python

```Python
pip install -r ./requirements.txt
python ./gui.py
```

## 其他文档

- [常见问题](./faq.md)
- [中继相关](./relay.md)

## 更新日志（important only）

- 修复文件夹遍历不选择的情况下出现自动选择文件的情况
- 新增转换中继链接

---

鸣谢：[SMMS图床](https://sm.ms)

电报交流群：[https://t.me/smmsuploader](https://t.me/smmsuploader)
