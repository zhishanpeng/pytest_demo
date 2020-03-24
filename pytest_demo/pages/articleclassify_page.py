from common.base import Base
from common.config import host
import allure

class ArticlclassifyPage(Base):
    文章分类 = ("xpath", '//*[@href="/xadmin/hello/articleclassify/"]')

    增加_文章分类 = ("xpath", '//*[@id="content-block"]/div[1]/div[2]/div/a')
    输入_分类 = ("id", "id_n")
    保存 = ("xpath", '//*[@id="articleclassify_form"]/div[2]/button')

    # 判断元素
    table = ("xpath", "//table")

    @allure.step("步骤：点击左侧文章分类导航")
    def click_classify_nav(self):
        '''点击左侧文章分类导航'''
        self.click(self.文章分类)

    @allure.step("步骤：编辑文章分类页面，编辑内容保存")
    def edit_classify(self, text="测试"):
        '''编辑文章分类'''
        self.click(self.增加_文章分类)
        self.send(self.输入_分类, text)
        self.click(self.保存)

    @allure.step("步骤：判断是否添加成功，返回布尔值")
    def is_edit_classify_success(self, text="测试"):
        '''判断是否添加成功，返回布尔值'''

        # 判断元素存在于table中
        table_text = self.get_text(self.table)
        return text in table_text

if __name__ == '__main__':
    from selenium import webdriver
    from web_pytest_x.common.base import Base
    from web_pytest_x.pages.login_page import LoginPage
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()

    result = web.is_login_success()
    print(result)

    # 编辑文章
    edit = ArticlclassifyPage(driver)
    edit.click_classify_nav()
    edit.edit_classify()
    # 判断结果
    result1 = edit.is_edit_classify_success()
    print(result1)
    driver.quit()


