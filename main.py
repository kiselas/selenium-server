from pyvirtualdisplay import Display
from seleniumwire import webdriver
import hashlib
from urllib.parse import urlparse
from urllib.parse import parse_qs


def get_query_params(url_path):
    parsed_url = urlparse(url_path)
    captured_values = parse_qs(parsed_url.query)
    return captured_values


def render_page(url, body=None, proxy=None):
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    driver = webdriver.Chrome()
    driver.get(url)
    body = str.encode(driver.page_source)
    driver.quit()
    display.stop()
    return body


