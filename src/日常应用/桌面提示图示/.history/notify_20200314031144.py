# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-03-14 02:55:59
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-14 03:11:44
@FilePath: \桌面提示图示\notify.py
@Version: 1.0
@Description: 
'''

import PySimpleGUI as sg
import win32gui
from selenium import webdriver


def notify():
    driver = webdriver.Chrome()
    elements = driver.find_elements_by_id("notification-count")
    if elements != []:
        try:
            count = int(elements[0].text)
        except:
            count = 0
        if count > 0:
            sg.SystemTray().notify('Notify', f'{count} new messages')

————————————————
原文作者：Jason990420
转自链接：https://learnku.com/articles/41712#reply132886
版权声明：著作权归作者所有。商业转载请联系作者获得授权，非商业转载请保留以上作者信息和原文链接。