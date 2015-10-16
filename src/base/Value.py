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
    ADDRESS_IP = "http://172.29.129.204:8091/thca"
    #login
    LOGIN_ID = ["servicecodename","username","userpwd_c","checkCode"]
   
    LOGIN_DICT = {LOGIN_ID[0]:"newobt",#admin
                  LOGIN_ID[1]:"testliu",#123456
                  LOGIN_ID[2]:"111111",
                  LOGIN_ID[3]:"tsts"
    }
     
    BASE_MSG =[u"创建地区",u"地区列表"]
     
    CREAT_AREA_ID = ["areaName","areaCode","cityPinYin","deliverScopeTip","parentAreaId0","areaType"]
    #创建地区 
    CREAT_AREA_DICT = { CREAT_AREA_ID[0]:"rtTest",#地区名称
                        CREAT_AREA_ID[1]:"rat",#123456
                        CREAT_AREA_ID[2]:"rtt", #城市拼音
                        CREAT_AREA_ID[3]:u"全国",
                        CREAT_AREA_ID[4]:u"中国大陆",
                        CREAT_AREA_ID[5]:u"国际类型"}#运送范围
    
    USER_MSG= [u"创建用户",u"用户列表"]
    
    CREAT_USER_ID =["loginName","loginPassword","confirmLoginPassword","email","contact","telphone"]
    
    CREAT_USER_DICT = {CREAT_USER_ID[0]:"testtest123",
                       CREAT_USER_ID[1]:"testtest123",
                       CREAT_USER_ID[2]:"testtest123",
                       CREAT_USER_ID[3]:"111@ddd.com",
                       CREAT_USER_ID[4]:"wang",
                       CREAT_USER_ID[5]:"12331231234",
                       }
    
    CREAT_USER_SELECT_ID = ["roleId","userParentAreaId0"]
    CREAT_USER_SELECT_DICT ={CREAT_USER_SELECT_ID[0]:u"管理员",
                             CREAT_USER_SELECT_ID[1]:u"中国大陆",
                             }

    LEFT_FRAME = "menu-frame"
    RIGHT_BODY = "main-frame"

#     obj = Web_method.Web_method()
#     browser_firefox= obj.open_url(PROFILE_DIR)
#     now_handle = obj.get_handle(browser_firefox)
#     $logincalss = decode("utf-8",$logincalss);//将汉字强制转换成utf-8格式的放到变量$logincalss中

    





