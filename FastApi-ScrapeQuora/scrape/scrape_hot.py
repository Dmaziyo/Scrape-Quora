from bs4 import BeautifulSoup
import requests, json
from utils.get_cookies import get_zhihu_cookies
from bs4 import BeautifulSoup


class HotMsg:
    def __init__(self, title, content, heat, img_src, a):
        self.title = title
        self.content = content
        self.heat = f'{heat}热度'
        self.img_src = img_src
        self.a = a

    def __repr__(self):
        return f'title:{self.title};content:{self.content};heat:{self.heat};img_src:{self.img_src};href:{self.a}'


def scrape_hot_text():
    url = 'https://www.zhihu.com/hot'
    session = requests.session()
    session.verify = False
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'
    }
    cookies_dict = dict()
    with open("cookies.txt", "r") as fp:
        # json.losd()就是读取的意思，fp是IO类型，不是字符串，json.loads()才是把字符串转换为python字典格式，需要注意
        cookies = json.load(fp)
        print('加载cookie成功')
        for cookie in cookies:
            # cookies最终是字典类型，保存的selenium的cookies是列表，列表里的每个元素是一个字典，这里的每个字典的name和value组成为requests的cookies
            cookies_dict[cookie['name']] = cookie['value']

    html_text = session.get(url, cookies=cookies_dict).text
    soup = BeautifulSoup(html_text, 'lxml')
    hot_sections = soup.find_all('section', class_="HotItem")
    hot_msgs = []
    for hot_section in hot_sections:
        div_content = hot_section.find('div', class_="HotItem-content")
        title = div_content.a.h2.text
        p = ''
        img = ''
        heat = ''
        href = ''
        if div_content.a.p:
            p = div_content.a.p.text
        if div_content.find('div', class_="HotItem-metrics HotItem-metrics--bottom"):
            heat = str(div_content.find('div', class_="HotItem-metrics HotItem-metrics--bottom").text).replace('分享','')
        elif div_content.find('div', class_="HotItem-metrics"):
            heat = str(div_content.find('div', class_="HotItem-metrics").text).replace('分享', '')
        if hot_section.find('a', class_="HotItem-img"):
            img = hot_section.find('a', class_="HotItem-img").img["src"]
        if div_content.a['href']:
            href = div_content.a['href']

        hotmsg = {
            "title": title,
            "p": p,
            "img": img,
            "heat": heat,
            "href": href
        }
        hot_msgs.append(hotmsg)
    ret = {
        "data": hot_msgs
    }
    return ret
