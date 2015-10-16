#coding=utf-8
'''
用于循环定时启动

@author: wanglong
'''

import os,time
k=1
except_time = '19_54'
print(u"开始进入测试")
file_path = os.getcwd()
while k <2:
    now_time=time.strftime('%H_%M')
    if now_time == except_time:
        print u"开始运行脚本"
        
        os.chdir(file_path)
        os.system('Python Main.py') 
        print u"结束运行脚本"
        break
    else:
        time.sleep(10)
        print now_time