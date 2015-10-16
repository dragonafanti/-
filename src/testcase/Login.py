#coding= utf-8
'''
Created on 201509018

@author: wanglong
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from base import *
from collections import _field_template
import xlrd

class Test(unittest.TestCase):


    def setUp(self):
        aa = webdriver.FirefoxProfile("D:\FirefoxProfilesDir")
        self.driver = webdriver.Firefox(aa)
        self.driver.implicitly_wait(30)
        self.base_url = "http://obttst.btravelplus.com:8091/"
        self.verificationErrors = []
        self.accept_next_alert = True
        pass

    def tearDown(self):
#         self.driver.quit()
        pass

    def test_1_me(self):
       
#         self.driver.get(self.base_url)
#         self._obj = Tools.Tools()
#         self._obj.input_send_key(self.driver,By.ID,vvvv._id, vvvv._dict)
#         self._obj.input_send_key(self.driver,By.NAME,vvvv._name, vvvv._dict)
#         self.driver.find_element(By.NAME,'submit').click()
#         time.sleep(10)
#         _va_= self.driver.find_element(By.XPATH,".//*[@id='tablist']/tbody/tr[2]/td[2]")
#         _cl_= self.driver.find_element(By.CLASS_NAME, "table responsive")
#         print _cl_.text

        
        _file = File_method.File_method()
        
        print excel_name,_file
        _excel = Excel_rd.Excel_rd()
        _tabel = _excel.get_excel_table(excel_name+_file, "Sheet1")
        _eee_= _excel.get_row_value(_tabel, 1)
        print _eee_




#         self.assertEqual(eee, '差旅专家在线预订系统111', "成功打开网站")
      
#         self.assertTrue(eee, "我是断言出来的")
#         print By.ID
#         self.driver.find_element_by_id(id_)
#         self.driver.find_element_by_name(name)
#         self.driver.find_element(By.NAME, value)
        
        
        
#         for i,j in _id,_value:
#             self.driver.find_element_by_id(i).clear()
#             self.driver.find_element_by_id(i).send_keys(j)
#         driver.find_element_by_id("username").clear()
#         driver.find_element_by_id("username").send_keys("testliu")
#         driver.find_element_by_id("userpwd_c").clear()
#         driver.find_element_by_id("userpwd_c").send_keys("111111")
#         driver.find_element_by_name("checkCode").clear()
#         driver.find_element_by_name("checkCode").send_keys("citsky20150602")
#         driver.find_element_by_name("submit").click()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()