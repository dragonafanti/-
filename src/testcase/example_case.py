#coding= utf-8
'''
用例例子

@author: wanglong
'''
import unittest
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from base import *
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Example_Case(unittest.TestCase):


    def setUp(self):
       self._web_obj = Web_method.Web_method()
       self._file_method = File_method.File_method()
       self._value = Value.Value()
       self._driver = self._value.browser_firefox

    def test_example(self):
        u"""测试用例例子"""
        print(u"欢迎使用测试模板")


    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()