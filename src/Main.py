# -*- coding: utf-8 -*-
'''
Created on 20150819

@author: wanglong
'''
import unittest,doctest
import sys,time,os
import all_test_list
import HTMLTestRunner
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
    print(u"开始" )  
    
    testsuite = doctest.DocTestSuite()
    alltestnames = all_test_list.caselist()
    for test in alltestnames:
        testsuite.addTest(unittest.makeSuite(test))
    return testsuite

# suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
# suite.addTest(Login.Login("testLogin_Login)
# runner = unittest.TextTestRunner()
if __name__ == "__main__":
    
    file_path = os.getcwd()
    file_path = file_path[0:len(file_path)-3]
    loca_time= time.strftime("%Y-%m-%d %H_%M", time.localtime())
    save_name = 'result_'+loca_time
    report_path = file_path+'report\\'
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

