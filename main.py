from pyvirtualdisplay import Display
from selenium import webdriver
import hashlib
from urllib.parse import urlparse
from urllib.parse import parse_qs


def get_query_params(url_path):
    parsed_url = urlparse(url_path)
    captured_values = parse_qs(parsed_url.query)
    return captured_values


def get_page(url):
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    driver = webdriver.Chrome()
    driver.get(url)
    body = str.encode(driver.page_source)
    file_name = hashlib.md5(driver.current_url.encode()).hexdigest()

    with open(f'./{file_name}.html', 'w') as f:
        f.write(driver.page_source)

    driver.quit()
    display.stop()
    return body


