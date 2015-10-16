#coding= utf-8

'''
Created on 2015��9��25��

@author: wanglong
'''
from selenium.common.exceptions import NoSuchElementException
import time
class Tools():
#     def input_send_key(self,driver,_dict):
# #       for i,j in _id,_value:
#         for v,k in _dict.items():
#             driver.find_element_by_id(v).clear()
#             driver.find_element_by_id(v).send_keys(k)
    def input_send_key(self,driver,_by,_list,_dict):
        '''
                输入。。。。
        :param driver:浏览器句柄
        :param _by:By.id...
        :param _X:数组
        :param _dict:
        '''
        
        for v in _list:
#             if _by == "id":
#                 driver.find_element_by_id(v).clear()
#                 driver.find_element_by_id(v).send_keys(_dict[v])
#             elif _by =="name":
#                 driver.find_element_by_name(v).send_keys(_dict[v])     
        
            flag = False
            try:
                print "通过"+_by+"寻找"+v+"输入值"+_dict[v]
                _find_ele = driver.find_element(_by,v)
                _find_ele.send_keys(_dict[v])
            except NoSuchElementException:
                print u"找不到元素呀呀"
            time.sleep(2)
                
            
                
