# -*- coding: utf-8 -*-
# '''
# Created on 2015��8��24��
# 
# @author: wanglong
# '''
from selenium import webdriver
import time,types,os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import sys
from base import File_method
from base import Excel_rd 
reload(sys)
sys.setdefaultencoding('utf-8')

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
        '''
                          根据IP地址访问页面
        :param dr:浏览器
        :param ip:需要转入的IP地址
        '''
        
        print("输入IP地址")
        dr.get(ip)
        time.sleep(3)
    def get_step_desc(self,step_list):
        '''
                        返回行第一列的内容：用例步骤描述信息
        :param step_list:excel整行内容
        '''
        return str(step_list[0])
    def get_step_by_how(self,step_list):
        '''
                        返回行第2列的内容：对于元素查找，通过的方式
        :param step_list:excel整行内容
        '''
        return str(step_list[1])
    def get_step_key_name(self,step_list):
        '''
                        返回行第3列的内容：关键字的值内容
        :param step_list:excel整行内容
        '''
        return str(step_list[2])
    def get_step_fun(self,step_list):
        '''
                        返回行第4列的内容：选择本行的目的来调用相应的方法
        :param step_list:excel整行内容
        '''
        return str(step_list[3])
    def get_step_value(self,step_list):
        '''
                        返回行第5列的内容：需要输入或者比对的具体内容值
        :param step_list:excel整行内容
        '''
        return str(step_list[4])
    
    def find_element(self,dr,step_list,by_how=""):
        '''
                         寻找元素
        :param dr:浏览器
        :param step_list: 元素关键字,可以是字符，或者list转进来的列表类型，一般为4个值（by,元素名称，how,输入值）
        :param by_how:查询方式，list参数可省略
        '''
           
        try:       
            if type(step_list)== types.StringType:
                _element_key_ = step_list
                _element_ = dr.find_element(by_how, _element_key_)  
            else:
                _by_how_ = self.get_step_by_how(step_list)
                _element_key_ = self.get_step_key_name(step_list)
                _element_ = dr.find_element(_by_how_,_element_key_)
            print(u"关键字"+_element_key_)
            return _element_                
        except NoSuchElementException :
            self.save_error_png(dr, _element_key_)
            print(u"寻找关键字"+_element_key_+u"失败")        
            return False

    def input_by_dict(self,dr,by_how,itme_id,itme_dict,range_num):
        '''
                        根据参数进行输入操作。支持字典多循环操作。或者单独字符一次操作
        :param dr:浏览器    
        :param by_how: 查找方法
        :param itme_id: 查找关键字的数组，
        :param itme_dict: 输入与数组相对应的字典
        :param range_num: 执行的次数（相对数组）
        '''
       
        try:  
            for id_index in range(range_num):
        
                print(itme_id[id_index]+" "+itme_dict.get(itme_id[id_index]))
                _element_ = self.find_element(self, dr, itme_id[id_index],by_how )  
                _element_.clear()
                _element_.send_keys(itme_dict.get(itme_id[id_index])) 
        
        except NoSuchElementException :
            self.save_error_png(dr, itme_id[id_index])
      
    def input_by_list(self,dr,step_list,by_how="",send_key =""):
        '''
                      在指定地点输入指定内容 
        :param dr:浏览器
        :param step_list:元素关键字,可以是字符，或者list转进来的列表类型，一般为4个值（by,元素名称，how,输入值）
        :param by_how: 查询方式，list参数可省略
        :param send_key:输入内容。list参数可省略
        '''
        
        try:
            _element_= self.find_element(dr, step_list,by_how)
            if type(step_list)== types.StringType:
                _send_key_ = send_key
            else:
                _send_key_ = self.get_step_value(step_list)
            _element_.clear()
            _element_.send_keys(_send_key_)
        except AttributeError:
            print u"没有send_key属性，无法输入"+_send_key_
            self.save_error_png(dr, _send_key_)
                
        
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
            self.save_error_png(dr, itme_id[id_index])
            
     
    def click_by_list(self,dr,step_list,by_how=""):
        '''
                        通过元素点击操作
        :param dr:浏览器
        :param step_list: 元素关键字,可以是字符，或者list转进来的列表类型，一般为4个值（by,元素名称，how,输入值）
        :param by_how: 查询方法
        '''
        try:
            _element_ = self.find_element(dr, step_list,by_how)
            _element_.click()              
        except AttributeError :
            print u"无法进行cilck操作"
            
    def set_other_auto(self,dr,step_list):
         
        try:
            eval(self.get_step_value(step_list))
            return True
        except NoSuchElementException:
            return True       
   
        
    def switch_default(self,dr):
        '''
                        切换到默认框架
        :param dr:
        '''
        return dr.switch_to_default_content()   
                        
    def switch_frame(self,dr,step_list):#切换框架
        '''
                        切换指定框架
        :param dr:浏览器
        :param _frame_name: 框架部分名称
        '''
        if type(step_list)== types.StringType:
            _frame_name = step_list
        else:
            _frame_name = self.get_step_value(step_list)
        dr.implicitly_wait(20)
        dr.switch_to_default_content()
        return dr.switch_to_frame(_frame_name)
    
    def wait_handle(self,dr,handle):#处理窗口句柄
        for i in range(1,30):
            now_handle = dr.current_window_handle
            time.sleep(3)
            if handle != now_handle:
                dr.switch_to_window(handle)
                break
            
    def save_error_png(self,dr,error_name):
        '''
                        截图 取当前时间加命名
        :param dr:浏览器内容
        :param error_name:截图姓名
        '''
        file_path = os.getcwd()
        path = file_path[0:len(file_path) - 3]
        _save_address = path +"errorpng\\" 
        loca_time= time.strftime("%Y%m%d%H%M%S", time.localtime())
        dr.get_screenshot_as_file(_save_address+loca_time+"_"+error_name+".png")
       
    def is_element_present(self,dr,step_list, by_how =""):
        '''
                         判断元素是否存在，不存在则截图
        :param dr: 浏览器
        :param step_list:可以是一个列表，也可以是单独一个字符串，如果是字符串，必须配合by_how
        :param by_how:关键字的属性， id,name等等
        '''
        
        if self.find_element(dr,step_list,by_how):
            return True
        else:
            return False
        
   
    def is_title_present(self,dr,step_list):
        '''
                        判断获得标题是否为期望标题
        :param dr:
        :param get_title:期望标题
        '''
        
        if type(step_list)== types.StringType:
            expect_title = step_list
        else:
            expect_title = self.get_step_value(step_list)
            _now_title_ =  dr.title
        if _now_title_ == expect_title:
            print u"标题为: "+_now_title_
            return True
        else:
            print u"实际标题为："+_now_title_+u"与预期标题："+expect_title+u"不符"
            self.save_error_png(dr, expect_title)
            return False
    
    def is_text_present(self,dr,step_list,by_how=""):
        '''
                        判断从页面元素获得的文本是否为期望内容
        :param dr:
        :param step_list:期望标题
        '''
        if type(step_list)== types.StringType:
            expect_text = step_list
        else:
            expect_text = self.get_step_value(step_list)
        _element_ = self.find_element(dr,step_list,by_how)
        if _element_:
            try:
                _now_text_=_element_.text
                if _now_text_ == expect_text: 
                    print u"文本信息为: "+_now_text_
                    return True
                else:
                    self.save_error_png(dr, expect_text)
                    print u"实际内容为："+_now_text_+u" 和预期不匹配"
                    return False
            except AttributeError:
                print u"页面元素不存在text属性"
        else:
            return False
        
    def wait_sleep(self,step_list):
        '''
                                转换成等待时间
        :param step_list:行数据
        '''
        _sleep_time_ = int(self.get_step_value(step_list))
        time.sleep(_sleep_time_)
        return True
        
    def implicitly_wait(self,dr,step_list):
        '''
                                隐性等待时间
        :param dr:
        :param step_list:行数据
        '''
        _sleep_time_ = int(self.get_step_value(step_list))
        dr.implicitly_wait(_sleep_time_)
        return True
    
    def switch_alert(self,dr,get_type):
        if get_type == "text" :
            return dr.switch_to_alert().text()
           
    def run_list_step(self,dr,step_list):
        '''
                            将接受的行的内容内的关键字找出对应的执行方法
        :param dr:
        :param step_list:
        '''
        _key_ = self.get_step_fun(step_list)
        self._file = File_method.File_method()
        _value_ = self._file.get_config_opt(_key_)
        if _value_:
            _result_ = eval(_value_)
        else:
            _result_ = False
        return _result_
    
    def run_general_case(self,dr,file_name,file_sheet):
        '''
                        运行的普通case
        :param dr:
        :param file_name: wps文件名
        :param file_sheet:sheet页
        '''
        self._excel = Excel_rd.Excel_rd()
        self._case = self._excel.sheet_to_dict(file_name,file_sheet)
        for step_list in self._case:
            _case_desc_ = self.get_step_desc(step_list)
            print _case_desc_
            _run_type_ = self.get_step_fun(step_list)
            time.sleep(2)
            _result_ = self.run_list_step(dr, step_list)
            if "find" in _run_type_ and _result_ == False:
                return _result_          
        return True    