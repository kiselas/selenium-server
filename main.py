from pyvirtualdisplay import Display
from seleniumwire import webdriver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results.backends import RedisBackend
from dramatiq.results import Results
redis_broker = RedisBroker(host="redis")
redis_backend = RedisBackend(host="redis")
redis_broker.add_middleware(Results(backend=redis_backend))

dramatiq.set_broker(redis_broker)


def get_query_params(url_path):
    parsed_url = urlparse(url_path)
    captured_values = parse_qs(parsed_url.query)
    return captured_values


@dramatiq.actor(
    store_results=True,
    max_backoff=100,
    max_retries=3,
    queue_name="selenium-queue",
)
def render_page(url, body=None, proxy=None):
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    opt = webdriver.ChromeOptions()
    # opt.add_argument("--headless")
    opt.add_argument("--disable-xss-auditor")
    opt.add_argument("--disable-web-security")
    opt.add_argument("--disable-dev-shm-usage")
    opt.add_argument("--allow-running-insecure-content")
    opt.add_argument("--no-sandbox")
    opt.add_argument("--disable-setuid-sandbox")
    opt.add_argument("--disable-webgl")
    driver = webdriver.Chrome(options=opt)
    driver.get(url)
    body = driver.page_source
    if body:
        response_result = driver.page_source
        driver.quit()
        display.stop()
        return response_result
    else:
        return {'Error': 'empty page'}


