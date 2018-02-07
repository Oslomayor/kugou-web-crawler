# kugou-web-crawler
# 1:05PM, Feb 7th, 2018 @ CE, 9/-3, very cold
# 爬取酷狗 top 500 排行榜的音乐信息
# 爬取的信息：歌手、歌曲名称、歌曲时长
# http://www.kugou.com/yy/rank/home/1-8888.html?from=rank
# http://www.kugou.com/yy/rank/home/2-8888.html?from=rank
# ...
# http://www.kugou.com/yy/rank/home/23-8888.html?from=rank
# 共23个页面，498条信息，酷狗TOP500 2018-2-1 更新

from bs4 import BeautifulSoup
import requests
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def get_info(url):
    global count
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 歌手、歌曲名称、歌曲链接在同一段 html 代码中
    # 歌曲时长在另一段 html 代码中
    infomations = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    songTimes = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for infomation, songTime in zip(infomations, songTimes):
        href = infomation.get('href')
        singer = infomation.get('title')
        songTime = songTime.getText().strip()
        count += 1
        print('歌曲{count}：\n'.format(count=count)+'链接：' + href + '\n' + '歌曲：' + singer + '\n' + '时长：' + songTime + '\n')

def main():
    global count
    count = 0
    urls = ['http://www.kugou.com/yy/rank/home/{page}-8888.html?from=rank'.format(page=page) for page in range(1, 24)]
    print('酷狗TOP500 2018-2-1 更新')
    for url in urls:
        print('on page:'+url)
        get_info(url)
        time.sleep(1)


if __name__ == '__main__':
    main()
