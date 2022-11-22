# FastApi-ScrapeQuora
爬取知乎的接口

## FastApi-ScrapeQuora
- 配置<br/>
pip install -r requirements.txt
- 在number.py文件修改成你的qq账号和密码<br/>
uvicorn main:app --reload <br/>
Tips:建议直接用pycharm打开,配置python环境

1. 访问/start获取cookie
2. 访问/hot可获取热搜词条
3. 访问/video可获取推荐视频内容


## Client
npm install <br/>
npm run serve

## 结果展示
- 访问接口/hot
![Snipaste_2022-11-22_11-23-15](https://user-images.githubusercontent.com/74136983/203211473-edd6846b-451d-479a-85d4-1be33fde9ec7.jpg)
- 访问接口/video
![Snipaste_2022-11-22_11-24-39](https://user-images.githubusercontent.com/74136983/203211644-33e7a561-860e-4972-b1a3-12c20e03b1a4.jpg)

- 页面展示
![1](https://user-images.githubusercontent.com/74136983/203212060-89fddccb-49de-45b2-9c2d-266f6c86c5b5.jpg)
![Snipaste_2022-11-22_11-31-46](https://user-images.githubusercontent.com/74136983/203212544-2ad29a06-eeae-42e8-9f67-646fb78d6425.jpg)
