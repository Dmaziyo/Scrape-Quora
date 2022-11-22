import time

import json

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

from utils.Options import Setting


def traverse_video(video_sections,v_infos):
    for video_section in video_sections:
        href = video_section.a['href']
        img = video_section.a.div.img['src']
        title = video_section.h2.a.text
        creator_icon = video_section.find('div', class_='css-vylitd').img['src']
        creator = video_section.find('div', class_='css-1nne2a7').text
        v_time = video_section.find('div', class_='css-vurnku').text
        views = video_section.find('div', class_='css-18b1ycz').text
        v_info = {
            "title": title,
            "img": img,
            "creator": creator,
            "creator_icon": creator_icon,
            "views": views,
            "v_time": v_time,
            "href": f'https://www.zhihu.com{href}'
        }
        v_infos.append(v_info)

def scrape_video():
    set1 = Setting()
    url = 'https://www.zhihu.com/zvideo'
    chrome = Chrome(options=set1.options)
    chrome.get(url)
    time.sleep(2)

    with open("cookies.txt", "r") as fp:
        # json.losd()就是读取的意思，fp是IO类型，不是字符串，json.loads()才是把字符串转换为python字典格式，需要注意
        cookies = json.load(fp)
        for cookie in cookies:
            chrome.add_cookie(cookie)
    chrome.refresh()
    time.sleep(2)
    soup = BeautifulSoup(chrome.page_source, 'lxml')

    video_sections1 = soup.find_all('div', class_="css-1tane06")
    video_sections2 = soup.find_all('div', class_="css-cazg48")
    v_infos = []
    traverse_video(video_sections1,v_infos)
    traverse_video(video_sections2,v_infos)

    chrome.close()
    ret = {
        "data":v_infos
    }
    return ret
