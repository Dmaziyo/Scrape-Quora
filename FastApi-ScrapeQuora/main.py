from fastapi import FastAPI
from utils.get_cookies import get_zhihu_cookies
from scrape.scrape_hot import scrape_hot_text
from scrape.scrape_video import  scrape_video
app = FastAPI()

#start-cmd: uvicorn main:app --reload

@app.get("/start")
async def root():
    try:
        get_zhihu_cookies()
        return {
            "code": 200,
            "msg": "get cookies succeed"
        }
    except Exception:
        return {
            "code": 405,
            "msg": "Cookie error"
        }
@app.get("/hot")
async def get_hot():
    try:
        msg= scrape_hot_text()
        return {
            "code": 200,
            "msg": msg
        }
    except Exception:
        return {
            "code": 405,
            "msg": "Cookie error"
        }

@app.get("/video")
async def get_hot():
    try:
        msg= scrape_video()
        return {
            "code": 200,
            "msg": msg
        }
    except Exception:
        return {
            "code": 405,
            "msg": "Cookie error"
        }