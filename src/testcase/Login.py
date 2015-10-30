#coding= utf-8
'''
Created on 2015.10.16

@author: wanglong
'''
import unittest
from base import *
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Login(unittest.TestCase):


    def setUp(self):
        self._value = Value.Value()
        self._excel = Excel_rd.Excel_rd()
        self._driver = self._value.browser_firefox
        
        self._web = Web_method.Web_method()
        self._web.access_ip(self._driver, self._value.ADDRESS_IP)
        self._driver.implicitly_wait(10)
    def tearDown(self):
        pass

       
                
    def test_case_1(self):
        u"""公司代码为空"""
        _result_ = self._web.run_general_case(self._driver, u"Login.et", "Case1")
        self.assertTrue(_result_, "公司代码为空测试失败")
        
    def test_case_2(self):
        u"""用户名为空"""
        _result_ = self._web.run_general_case(self._driver, u"Login.et", "Case2")
        self.assertTrue(_result_, "用户名为空测试失败") 
    def test_case_3(self):
        u"""用户密码为空"""
        _result_ = self._web.run_general_case(self._driver, u"Login.et", "Case3")
        self.assertTrue(_result_, "用户密码为空测试失败")       
                    
    def test_case_10(self):
        u"""正常登录是否成功"""
        _result_ = self._web.run_general_case(self._driver, u"Login.et", "Case10")
        self.assertTrue(_result_, "测试正常登录失败") 
        
        
        
        
        
        
        
                        
                
    def example_case_2(self):
        u"""正常登录是否成功"""
                         
        
        dr = self._driver
        self._case1 = self._excel.sheet_to_dict(u"Login.et", "Case1")
        _other_dict_ = {"1":"self._web.input_by_list(dr, 'username', 'id', _sendkey_)",
                        "2":"self._web.find_element(dr,'ui-dialog-content', 'class name').text",
                        "3":"print _eee_"}
        _vvv_ =["qew","testliu","wwqe123","/$%%"]
        for _sendkey_ in _vvv_:
            for _row_val_ in self._case1:
                _run_type_ = _row_val_[2]
                time.sleep(2)
#                 if"other"  in   _run_type_:
#                     _other_num_ = _row_val_[3]
# #                     print _other_dict_[_other_num_]
# #                     self._web.input_by_list(dr, "username", "id", _sendkey_)
#                     print _row_val_[3]
#                     eval(_row_val_[3])
#                 else:
                
                _resule_ = self._web.run_list_step(dr, _row_val_)
                if "find" in _run_type_:
                    self.assertTrue(_resule_, _run_type_+"判定失败")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()