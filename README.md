
# ![SMMS Uploader](https://i.loli.net/2019/02/10/5c5fc5fbe1018.png) SMMS Uploader 图床上传工具

![SMMS Uploader GUI](https://i.loli.net/2019/02/15/5c664a4168958.jpg)

<!-- TFSsIYDgiOHxCvk -->

## 文件解释

- `gui.py` GUI模块
- `smms.py` 图床上传模块
- `scanner.py` 文件扫描模块
- `ico.py` ICON文件
- `*save.txt` 上传成功文件列表（自动生成）
- `*fail.txt` 上传失败文件列表（自动生成）
- `*links.txt` CDN链接列表（自动生成）
- `ib.py` 测试文件（非必要文件）
- `del.py` 自动批量删除模块（非必要文件）
- `ico2b64.py` ICON转换模块（非必要文件）
- `build.bat` EXE文件生成批处理文件（非必要文件）

**自动生成的文件可能随版本更新而变动**

## 命令行模式

暂未开发

## GUI模式

都有GUI了不用解释了吧？

## EXE不能打开？

- 系统必须是Win7 SP1 或以上版本
- `缺少api-ms-win-crt-runtime-l1-1-0.dll`等错误提示请安装`KB2999226`补丁[微软官网下载](https://www.microsoft.com/en-us/download/details.aspx?id=49093)
- 其他情况请提交ISSUE以获得支持

## 额外依赖（具体依赖请自行查看源代码）

- urllib3
- pywin32

## 其他文档

- [常见错误及解决方案](./error.md)

## 更新日志（important only）

- 修复中文文件名无法上传的问题
- 修复文件过大情况下上传失败的问题
- 增加上传提示

---

鸣谢：[SMMS图床](https://sm.ms)

电报交流群：[https://t.me/smmsuploader](https://t.me/smmsuploader)

且用且珍惜！
