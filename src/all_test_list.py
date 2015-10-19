# -*- coding: utf-8 -*-
'''
测试用例列表，内容为类名

@author: wanglong
'''
from testcase import Login
from testcase import *



def caselist():
    alltestnames = [
#         example_case.Example_Case, 
        testcase.Login.Login,
#      


    ]
    print u"case 读取成功"
    
    return alltestnames
        