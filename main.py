from pyvirtualdisplay import Display
from selenium import webdriver
import hashlib
display = Display(visible=False, size=(1920, 1080))
display.start()

driver = webdriver.Chrome()
driver.get('https://bot.sannysoft.com/')
body = str.encode(driver.page_source)
file_name = hashlib.md5(driver.current_url.encode()).hexdigest()

with open(f'./{file_name}.html', 'w') as f:
    f.write(driver.page_source)

driver.quit()
display.stop()
