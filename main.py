from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from utils import url_shorter

app = FastAPI()

url_db = {}

class URLRequest(BaseModel):
    url: HttpUrl


@app.post("/", status_code=201)
async def shorten_url(request: URLRequest):
    """Create a short link"""

    url = str(request.url)
    short_url = url_shorter(url=url)
    url_db[short_url] = url
    return {"short_url": short_url}


@app.get("/{short_url_id}")
async def original_url(short_url_id: str):
    """Get original url"""

    original_url = url_db.get(short_url_id)
    if not original_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return {"original_url": original_url}
