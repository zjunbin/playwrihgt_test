"""
#-*- coding:utf--8 -*-
#@Time    :2025/10/17 14:19
#@Author  :zjunbin
#@File    :run.py
"""
import os.path

'''自动发现、收集、运行生成测试allure报告'''
'查看测试报告   allure serve ./allure_report/'

import pytest
path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
print(path)
allure_results= os.path.join(os.path.join(path,'playwright_test'),'allure-results')
print(allure_results)
pytest.main(['-s', '-v', f'--alluredir={allure_results}', '--clean-alluredir'])
# pytest.main(['-s', '-v', r'--alluredir=E:\djangoProject\playwright_test\allure_report', '--clean-alluredir'])