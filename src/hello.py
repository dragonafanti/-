#!/usr/bin/env python3  
#coding: utf-8  
from base import *
from selenium.webdriver.common.by import By
from xlrd.biffh import _cell_opcode_dict
import time
import string
_excel_file = Excel_rd.Excel_rd()
_web_method = Web_method.Web_method()
# _table= _excel_file.get_excel_table(u"登录.xlsx", u"Sheet1")
_file_ = File_method.File_method()
_as_ = _file_.csv_dict(u"登录.csv", 0, 1)
print _as_

