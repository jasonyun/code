# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-03-14 02:55:59
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-14 03:13:23
@FilePath: \桌面提示图示\notify.py
@Version: 1.0
@Description: 
'''

import PySimpleGUI as sg
import win32gui
from selenium import webdriver


def notify():
    driver = webdriver.Chrome()
    driver.get('https://learnku.com/python')
    elements = driver.find_elements_by_id("notification-count")
    if elements != []:
        try:
            count = int(elements[0].text)
        except:
            count = 0
        if count > 0:
            sg.SystemTray().notify('Notify', f'{count} new messages')


def enumWindowFunc(hwnd, windowList):
    """ win32gui.EnumWindows() callback """
    text = win32gui.GetWindowText(hwnd)
    className = win32gui.GetClassName(hwnd)
    title = 'chromedriver.exe'
    if title in text.lower() or title in className.lower():
        win32gui.ShowWindow(hwnd, False)
        print('chromedriver hide')
    title = 'Python 技术论坛 | 高品质的 Python 开发者社区'.lower()
    if title in text.lower() or title in className.lower():
        win32gui.ShowWindow(hwnd, False)
        print('learnku hide')
