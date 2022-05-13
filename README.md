# dezoomify-rs 批量处理脚本



dezoomify-rs：https://github.com/lovasoa/dezoomify-rs

本脚本使用 dezoomify-rs 批量下载文件，无需手动操作选择尺寸level。



#### 环境

python 3+



#### 使用说明

1. 将脚本 run-batch.py 放置 dezoomify-rs目录中
2. 下载地址写入url.txt， 一行一条url



#### 参数说明

- line 6 dezoomify-rs路径，默认同路径
- line 9 默认尺寸，自动确认下载 0 level 文件
- line 20 批量Url文件名，默认 url.txt
- line 29 间隔时间，随机0-30秒停顿下载，建议保留



#### 测试

Mac m1

测试地址：http://codh.rois.ac.jp/north-china-railway/search/metadata?station_id=553&page=5

20220513 对以上地址测试通过





