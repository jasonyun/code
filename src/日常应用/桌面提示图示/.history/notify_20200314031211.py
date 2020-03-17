# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-03-14 02:55:59
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-14 03:12:10
@FilePath: \桌面提示图示\notify.py
@Version: 1.0
@Description: 
'''

import PySimpleGUI as sg
import win32gui
from selenium import webdriver


def notify():
    driver = webdriver.Chrome()
    driver.get(https://learnku.com/)
    elements = driver.find_elements_by_id("notification-count")
    if elements != []:
        try:
            count = int(elements[0].text)
        except:
            count = 0
        if count > 0:
            sg.SystemTray().notify('Notify', f'{count} new messages')
