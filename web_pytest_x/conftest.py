from web_pytest_x.pages.login_page import LoginPage
from selenium import webdriver
import pytest
import time
from selenium.webdriver.chrome.options import Options


# 命令行参数

def pytest_addoption(parser):

    parser.addoption(
        "--headless", action="store",
        default='no', help='set chrome headless option yes or no'
    )


@pytest.fixture(scope="session")
def driver(request):
    """定义全局driver fixture，给其它地方作参数调用"""
    headless = request.config.getoption("--headless")
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    if headless == "yes":
        chrome_options.add_argument('--headless')    # 无界面
    _driver = webdriver.Chrome(chrome_options=chrome_options)

    # _driver = webdriver.Chrome()
    # # # 窗口最大化
    # _driver.maximize_window()

    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        _driver.quit()

    request.addfinalizer(end)
    return _driver


@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login()
    return driver

