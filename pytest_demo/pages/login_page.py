from common.base import Base
from common.config import host
import allure

login_url = host+"/xadmin/"

class LoginPage(Base):
    loc_1 = ("id", "id_username")            # 用户名
    loc_2 = ("id", "id_password")            # 密码
    loc_3 = ("xpath", "//*[text()='登录']")   # 登录按钮

    # 判断元素
    loc_4 = ("xpath", "//*[text()='后台页面']")

    @allure.step("步骤：登陆web")
    def login(self, username="admin", password="yoyo123456"):
        '''登录'''
        self.driver.get(login_url)
        self.send(self.loc_1, username)
        self.send(self.loc_2, password)
        self.click(self.loc_3)

    @allure.step("步骤：判断登录是否成功")
    def is_login_success(self):
        '''判断登录是否成功'''
        result = self.is_element_exist(self.loc_4)
        return result

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    web.login()

    result = web.is_login_success()
    print(result)
    driver.quit()