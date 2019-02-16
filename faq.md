# ![SMMS Uploader](https://i.loli.net/2019/02/15/5c6678567831c.jpg) SMMS Uploader 图床上传工具

## EXE不能打开？

- 系统需要Win7 SP1 或以上版本
- `缺少api-ms-win-crt-runtime-l1-1-0.dll`等错误提示请安装`KB2999226`补丁[微软官网下载](https://www.microsoft.com/en-us/download/details.aspx?id=49093)
- 其他情况请提交ISSUE以获得支持

## 无法解析服务器响应

请检查程序是否为最新版本，[最新版下载](https://github.com/jokin1999/SMMS_Uploader/releases)

## 常见错误中英对照

|英语|中文|解释|
|:-|:-|:-|
|File is empty.|文件是空的|空文件无法上传|
|File is too large.|文件大小超出限制|图床支持最大5M的文件|
|File has an invalid extension.|文件格式不支持|图床上传文件格式限制|
|Could not save uploaded file.|服务器无法保存文件|图床原因，可以稍候再试|
|Request Entity Too Large.|请求量过大|类似文件过大|
|No files were uploaded.|没有文件被上传|无法找到对应的文件|
|Failed to open file.|文件打开失败|无法打开或读取指定文件|

\*其他错误有尝试机制

## 其他问题

请在提交ISSUE
