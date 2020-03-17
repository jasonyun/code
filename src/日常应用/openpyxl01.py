# -*- encoding: utf-8 -*-
'''
@File    :   openpyxl01.py
@Time    :   2020/02/17 14:33:50
@Author  :   JoeYun 
@Version :   1.0
@description: 用openpyxl读写execl
'''

from openpyxl.reader.excel import load_workbook
import os


def execldemo():
    data = {
        "xh": "08",
        "bh": "113",
        "lwh": "专业办公会〔2020〕5号",
        "title": "江汉盐穴天然气储气库项目建设协调会纪要",
        "date": "2020/1/31"
    }
    data1 = ["09", "114", "专业办公会〔2020〕5号", "江汉盐穴天然气储气库项目建设协调会纪要", "2020/1/31"]
    wb = load_workbook(os.path.dirname(__file__) + "\公文.xlsx")
    sheet = wb.active
    sheet.append(data)
    wb.save(os.path.dirname(__file__) + "\公文.xlsx")


if __name__ == "__main__":
    execldemo()
