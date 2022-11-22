import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from utils.Options import Setting
from utils.number import login

set = Setting()


def get_zhihu_cookies():
    chrome = Chrome(options=set.options)
    chrome.get('https://www.zhihu.com/')

    #qq 登录
    chrome.find_element(By.XPATH, "//span[@class='Login-socialButtonGroup']/button[2]").click()
    # 切换到最新窗口

    chrome.switch_to.window(chrome.window_handles[-1])
    chrome.switch_to.frame("ptlogin_iframe")
    # 自动输入密码
    chrome.find_element(By.ID, 'switcher_plogin').click()
    chrome.find_element(By.ID, 'u').send_keys(login['user'])
    chrome.find_element(By.ID, 'p').send_keys(login['pwd'])
    chrome.find_element(By.ID, 'login_button').click()
    print('登录成功')
    time.sleep(20)
    chrome.switch_to.window(chrome.window_handles[-1])
    cookies = chrome.get_cookies()
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)
    time.sleep(1)
    chrome.close()
