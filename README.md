# FastApi-ScrapeQuora
爬取知乎的接口

## FastApi-ScrapeQuora
- 配置<br/>
pip install -r requirements.txt
- 在number.py文件修改成你的qq账号和密码<br/>
uvicorn main:app --reload

1. 访问/start获取cookie
2. 访问/hot可获取热搜词条
3. 访问/video可获取推荐视频内容


## Client
npm install 
npm run serve