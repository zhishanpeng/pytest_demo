import os,sys

sys.path.append(os.getcwd())
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')    # 无界面

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.cnblogs.com/yoyoketang/")
time.sleep(5)

print(driver.title)
print(driver.page_source)

driver.quit()