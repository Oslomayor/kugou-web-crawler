# kugou-web-crawler
### 爬取酷狗 top 500 排行榜的音乐信息  
### [](http://www.kugou.com/yy/rank/home/1-8888.html?from=rank)
#### 10:46PM, Feb 7th, 2018

1.完善了 txt 文件保存爬取结果, 结果见 results-kugou-top500.txt

2.解决了遇到的 UnicodeEncodeError 报错

这个问题爬取短租网时遇到过一次，之前采用 try 和 except 方式避开了

这次仔细研究了一下这个问题的原因，发现是由于文件操作函数 open() 的默认编码方式依赖于平台环境导致的，遇到 title 名为 'BIGBANG - BANG BANG BANG (뱅뱅뱅) (Korean Ver.)' 中的 '뱅뱅뱅' 出现 UnicodeEncodeError.

open 函数的原型是：

> ```
> open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
> ```

help(open) 返回的官方解释：

> ```
> In text mode, if encoding is not specified the encoding used is platform dependent:
> locale.getpreferredencoding(False) is called to get the current locale encoding.
> ```

从官方描述中发现，open() 函数默认的 encoding 参数取决于平台环境，我这边的 open() 函数的 encoding 参数默认是 'gbk'编码(win 10 专业版 64 位 10.0 版本10240 + pycharm 2017.3.1)
但是 'gbk' 不支持 '뱅뱅뱅' 这种字符，在 open() 函数中加上 encoding='utf-8' 这个参数就解决了.



#### 1:45PM, Feb 7th, 2018  

提取了共23个页面，498条信息，酷狗 TOP500 2018-2-1  
2点钟上课了，晚上回宿舍上传统计结果 txt 文件
