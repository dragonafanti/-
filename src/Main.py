# -*- coding: utf-8 -*-
'''
Created on 20150819

@author: wanglong
'''
import unittest,doctest
import sys,time,os
import all_test_list
import HTMLTestRunner
import ConfigParser
from base import *
from testcase import *

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
import mail_report

reload(sys)
sys.setdefaultencoding('utf-8')


        
def send_report(testreport):
    result_dir = testreport
    lists= os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    mail_report.send_mail(file_new)
    
def creat_testsuite():
    testsuite = doctest.DocTestSuite()
    _testcase_name_ = "\\testcase.ini"
    _sention_name_ = 'FILE_LIST'
    _excel_sheet_ = "Case_List"
    _config_ = ConfigParser.ConfigParser()
    _excel_ = Excel_rd.Excel_rd()
    _file_path_ = os.getcwd()+_testcase_name_
    _config_.readfp(open(_file_path_))
    _case_list_ = _config_.items(_sention_name_)
    for i in range(len(_case_list_)):#取list里的行数遍历
        _class_name_ = _config_.get(_sention_name_, "file"+str(i+1))
        print "文件"+_class_name_+"测试用例"+_class_name_
        _excel_table_ = _excel_.get_excel_table(_class_name_+".et", _excel_sheet_)
        _test_num_ = _excel_.get_row_number(_excel_table_)
        for _j_ in range(_test_num_):
            _test_case_ = _excel_.get_row_value(_excel_table_, _j_)
            print _test_case_[0]
            _temp_ = "testsuite.addTest("+_class_name_+'.'+_class_name_+"(\'"+_test_case_[0]+"\'))"
            if _test_case_[1]=="":
                eval(_temp_)
            else:
                for _k_ in range(int(_test_case_[1])):
                    eval(_temp_) 
    return testsuite

# def creat_testsuite():
#     print(u"开始" )  
#     
#     testsuite = doctest.DocTestSuite()
# #     alltestnames = all_test_list.caselist()
#     
#     _all_test_case_ = get_test_file_list()
#     for test in _all_test_case_:
# #         testsuite.addTest(unittest.makeSuite(test))
#         eval(test)
#     return testsuite



# suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
# suite.addTest(Login.Login("test_open_url"))
# runner = unittest.TextTestRunner()
if __name__ == "__main__":
    
    file_path = os.getcwd()
    file_path = file_path[0:len(file_path)-3]
    loca_time= time.strftime("%Y-%m-%d %H_%M", time.localtime())
    save_name = 'result_'+loca_time
    report_path = file_path+'\\report\\'
    file_name = report_path+save_name+'.html'
    fp = file(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=u'测试结果',
                description=u'测试报告'
                )

    test_suite = creat_testsuite()
    runner.run(test_suite)
#runner = unittest.TextTestRunner()
#     send_report(report_path)

