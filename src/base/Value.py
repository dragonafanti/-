# -*- coding: utf-8 -*-
'''
"变量位置"
@author: wanglong
'''
import datetime
# from testCase.ThcaMainTest import ThcaMainTest
# import ThcaProject
from selenium import webdriver
from base import Web_method
class Value():
    #openbrower
    #火狐浏览器属性设置位置
    PROFILE_DIR = "D:\FirefoxProfilesDir" 
    #accessIP
#     ADDRESS_IP = "http://obttst.btravelplus.com/"
    ADDRESS_IP= "http://221.239.122.19:8088/"
    #login
   
    LEFT_FRAME = "menu-frame"
    RIGHT_BODY = "main-frame"

    obj = Web_method.Web_method()
    browser_firefox= obj.open_url(PROFILE_DIR)
#     now_handle = obj.get_handle(browser_firefox)
#     $logincalss = decode("utf-8",$logincalss);//将汉字强制转换成utf-8格式的放到变量$logincalss中

    





