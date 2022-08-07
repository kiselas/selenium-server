from fastapi import FastAPI
from main import render_page
from fastapi.responses import HTMLResponse
import validators

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, i'm selenium renderer! 🐣"}


@app.get("/get_page/", response_class=HTMLResponse)
async def get_page(url=None, body=None, proxy=None):
    """
    A temporary alternative for checking pages through the browser
    :param url:
    :param body:
    :param proxy:
    :return: html response | error
    """
    if url and validators.url(url):
        response = render_page.send(url, body, proxy)
        return response.get_result(block=True)
    else:
        return {'Error': 'Invalid url'}


@app.post("/get_page/", response_class=HTMLResponse)
async def get_page(url=None, body=None, proxy=None):
    """
    Main function to handle http request to rendering page
    from url.
    :param url: str
    :param body: json
    :param proxy: str 0.0.0.0
    :return: response | error
    """
    if url and validators.url(url):
        response = render_page.send(url, body, proxy)
        return response
    else:
        return {'Error': 'Invalid url'}
