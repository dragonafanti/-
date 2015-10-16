# -*- coding: utf-8 -*-
# '''
# Created on 2015��8��24��
# 
# @author: wanglong
# '''
from selenium import webdriver
import time,types
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
SAVE_ADDRESS = "D:\\thca_result\\error_png\\"

class Web_method(object):
    def open_url(self,profile_dir):
        '''
        
                        使用火狐自定义的预设路径，来打开浏览器。 打开办法，开始-运行-firefox -p
        :param profile_dir: 火狐的预设路径 
        PROFILE_DIR = "D:\FirefoxProfilesDir"
        '''
        profile = webdriver.FirefoxProfile(profile_dir)
        self._driver = webdriver.Firefox(profile)
        self._driver.maximize_window()
        return self._driver
    
    def get_handle(self,dr):
       
        self.handle = dr.current_window_handle
        return self.handle
        
    
    def access_ip(self,dr,ip):#访问地址
        """
                        根据IP地址访问页面
        """
        print("输入IP地址")
        dr.get(ip)
        time.sleep(3)

    def find_element_by(self,dr,by_how,element):
            #寻找元素        
            try:
                print(u"寻找元素"+element)
                time.sleep(3)
                element_result = dr.find_element(by_how,element)                
            except NoSuchElementException :
                loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
                dr.get_screenshot_as_file(SAVE_ADDRESS+loca_time+"_"+element+".png")           
            return element_result

    def input_by_dict(self,dr,by_how,itme_id,itme_dict,range_num):
        #循环输入
        try:  
            if type(itme_id)== types.StringType:
                element = Web_method.find_element_by(self, dr, by_how, itme_id)  
                element.clear()
                element.send_keys(itme_dict)
            else:
                for id_index in range(range_num):
            
                    print(itme_id[id_index]+" "+itme_dict.get(itme_id[id_index]))
                    element = Web_method.find_element_by(self, dr, by_how, itme_id[id_index])  
                    element.clear()
                    element.send_keys(itme_dict.get(itme_id[id_index])) 
            
        except NoSuchElementException :
            loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
            dr.get_screenshot_as_file(SAVE_ADDRESS+loca_time+"_"+itme_id[id_index]+".png")
                
    def select_by_dict(self,dr,by_how,itme_id,itme_dict,range_num):
        #循环输入 
        try: 
            if type(itme_id)== types.StringType:
                element = Web_method.find_element_by(self, dr, by_how, itme_id)  
                element.clear()
                element.send_keys(itme_dict)
            else:      
                for id_index in range(0,range_num):
                
                    print(itme_id[id_index]+" "+itme_dict.get(itme_id[id_index]))
                    element = Web_method.find_element_by(self, dr, by_how, itme_id[id_index])  
                    Select(element).select_by_visible_text(itme_dict.get(itme_id[id_index]))                
        except NoSuchElementException :
#             loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
#             dr.get_screenshot_as_file(SAVE_ADDRESS+loca_time+"_"+itme_id[id_index]+".png")
            Web_method.save_error_png(dr, itme_id[id_index])
     
    def click_by(self,dr,by_how,element):
        #循环输入        
       
        try:
            element = Web_method.find_element_by(self, dr, by_how,element)  
            element.click()              
        except NoSuchElementException :
#             loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
#             dr.get_screenshot_as_file(SAVE_ADDRESS+loca_time+"_"+element+".png")
            Web_method.save_error_png(dr, element)
        
    def switch_frame(self,dr,left_frame):#切换框架
        dr.implicitly_wait(20)
#         dr.switch_to_window(handle)
        dr.switch_to_default_content()
        dr.switch_to_frame(left_frame)
    
    def wait_handle(self,dr,handle):#处理窗口句柄
        for i in range(1,30):
            now_handle = dr.current_window_handle
            time.sleep(3)
            if handle != now_handle:
                dr.switch_to_window(handle)
                break
            
    def save_error_png(self,dr,error_name):
        loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
        dr.get_screenshot_as_file(SAVE_ADDRESS+loca_time+"_"+error_name+".png")
         
    def is_element_present(self,dr, how, what):
        """判断元素是否存在，不存在则截图"""
        try: 
            dr.find_element(by=how, value=what)
        except NoSuchElementException, e: 
            loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
            dr.get_screenshot_as_file(SAVE_ADDRESS+loca_time+"_"+what+".png")
            Web_method.save_error_png(self, dr, what)
            return False
        return True
   
       
        