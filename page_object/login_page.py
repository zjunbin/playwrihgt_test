"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 14:02
#@Author  :zjunbin
#@File    :login_page.py
"""
from playwright.sync_api import expect
import pytest
from common.basepage import BasePage

log_button = "//a[@id='s-top-loginbtn']"
phone = 'get_by_role("textbox", name="手机号/用户名/邮箱")'
pwd = 'get_by_role("textbox", name="密码")'
bt = 'get_by_role("checkbox", name="阅读并接受")'
bd  = "//*[@id='chat-submit-button']"
loca = "//*[@id='chat-textarea']"

class LoginPage(BasePage):

    def login_page(self, value):
        # self.click_ele(locator=log_button)
        self.page.wait_for_timeout(2000)
        self.fill_value(locator=loca,value=value)
        self.page.wait_for_timeout(2000)



    def assert_(self):
        expect(self.locator(locator=bd)).to_be_visible()
