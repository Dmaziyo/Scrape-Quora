from selenium.webdriver import  ChromeOptions
class Setting:
    def __init__(self):
        self.options = ChromeOptions()
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('-–ignore-certificate-errors')
        self.options.add_argument('--start-maximized')
        # self.options.add_argument('user-agent='+random_ua())
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 屏蔽webdriver特征
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--headless")