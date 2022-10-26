import time
import random
import asyncio
import aiohttp
import requests
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup

USER_AGENT_LIST = [
    'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
    'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
    'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
    'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
    'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
    'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
    'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
    'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
]

headers = {'User-Agent': random.choice(USER_AGENT_LIST)}

title = []
rating = []
visit_url = []
douban_url = []


def sync_douban(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        return None


async def async_douban(url):
    print(url, time.thread_time())
    async with asyncio.Semaphore(100):  # 并发控制
        conn = aiohttp.TCPConnector(limit=30)  # 连接池限制
        async with aiohttp.ClientSession(connector=conn) as session:
            async with session.get(url, headers=headers) as resp:
                await parse_tag(await resp.text())
                print(time.thread_time())


async def parse_tag(text):
    soup = BeautifulSoup(text, 'lxml')
    # html = soup.prettify()

    # meta = soup.find('div', attrs={"class": "meta"})
    # author = meta.find('a').get_text()
    # author = "".join(author.split())
    # created_at = meta.find('span').get_text()

    # movie_list = soup.select("div .title")
    movie_list = soup.find_all("div", attrs={"class": "title"})
    # print(movie_list[0].a.get('href'))
    rating_list = soup.find_all("span", attrs={"class": "rating_nums"})
    video_url = soup.find_all("a", attrs={"class": "doulist-video-item"})
    for index, item in enumerate(movie_list):
        a_tag = item.a
        _url = a_tag.get("href")
        douban_url.append(_url)

        _title = a_tag.get_text()
        # _title = "".join(_title.split())
        _title = _title.strip()
        title.append(_title)

        _rating = rating_list[index].get_text()
        rating.append(float(_rating))

        _video_url = video_url[index].get("href")
        visit_url.append(_video_url)


if __name__ == "__main__":
    url = 'https://www.douban.com/doulist/161656/?start={}'
    html = sync_douban(url)
    htmlObj = etree.HTML(html)
    meta = htmlObj.xpath('//div[@class="meta"]')[0]
    author = meta.xpath('./a/text()')[0]
    author = "".join(author.split())
    # created_at = meta.xpath('./span/text()')[0]
    # created_at = " ".join(created_at.split())
    total_page = htmlObj.xpath('//span[@class="thispage"]/@data-total-page')[0]
    tasks = [asyncio.ensure_future(async_douban(url.format(i))) for i in range(0, int(total_page) * 25, 25)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    _dict = {"电影名称": title, "豆瓣链接": douban_url, "播放链接": visit_url, "豆瓣评分": rating}
    data = pd.DataFrame(_dict)
    data.to_excel('豆瓣（这些片子我给六颗星）.xlsx', sheet_name="作者：" + author, engine='xlsxwriter', index=False)
