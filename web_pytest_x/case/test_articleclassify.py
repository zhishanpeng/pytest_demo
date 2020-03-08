from web_pytest_x.pages.login_page import LoginPage
from selenium import webdriver
from web_pytest_x.common.base import Base
from web_pytest_x.pages.login_page import LoginPage
from web_pytest_x.pages.articleclassify_page import ArticlclassifyPage
import pytest
from web_pytest_x.common.read_yml import readyml
import os
import allure

# testdata = [
#     ("测试", True),
#     ("aaaaaaaa", True),
#     ("11111", True)
# ]

ymlpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "articleclassify.yml")
print(ymlpath)
testdata = readyml(ymlpath).get("article_testdata")
print(testdata)

@allure.feature("文章分类页面")
class TestArticleclassify():
    '''文章分类页面'''

    @allure.story("编辑文章分类，输入中文，编辑成功")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-3-1.html")
    @pytest.mark.parametrize("test_input, expect", testdata)
    def test_edit_x(self, login, test_input, expect):
        '''前置条件:1.先登陆
        step1: 点文章分类导航标签
        step2: 编辑页面输入，分类名称，如:文学
        step3: 点保存按钮 ->保存成功
        '''
        driver = login
        # 实例化edit页面
        edit = ArticlclassifyPage(driver)
        # 点左侧导航栏
        edit.click_classify_nav()
        # 编辑
        edit.edit_classify(test_input)
        # 判断结果
        result1 = edit.is_edit_classify_success(test_input)
        print(result1)   # 实际结果
        # 断言
        assert result1 == expect

    @allure.story("编辑文章分类-输入重复的分类，保存失败，不能添加重复的")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-5-1.html")
    def test_edit_classify(self, login):
        '''重复编辑文章分类
        step1: 编辑“计算机”
        step2: 保存
        step3: 再次编辑“计算机”
        step4: 保存--》保存失败
        '''
        driver = login
        # 实例化edit页面
        edit = ArticlclassifyPage(driver)
        # 点左侧导航栏
        edit.click_classify_nav()
        # 编辑
        edit.edit_classify("计算机")
        # 判断结果
        result1 = edit.is_edit_classify_success("计算机")
        print(result1)

        # 重复编辑
        edit.click_classify_nav()
        # 编辑
        edit.edit_classify("计算机")
        # 判断结果
        result2 = edit.is_edit_classify_success("计算机")
        print(result2)

        # 断言
        assert not result2



    # def test_edit_classify(self):
    #     '''增加分类文章'''
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     web = LoginPage(driver)
    #     web.login()
    #
    #     result = web.is_login_success()
    #     print(result)
    #
    #     # 编辑文章
    #     edit = ArticlclassifyPage(driver)
    #     edit.click_classify_nav()
    #     edit.edit_classify()
    #     # 判断结果
    #     result1 = edit.is_edit_classify_success()
    #     print(result1)
    #     driver.quit()
    #
