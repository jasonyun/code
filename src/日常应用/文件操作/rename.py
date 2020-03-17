# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-02-16 20:38:29
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-04 21:01:23
@FilePath: \文件操作\rename.py
@Version: 1.0
@Description: 
'''

# -*- encoding: utf-8 -*-
'''
@File    :   rename.py
@Time    :   2020/02/16 20:40:25
@Author  :   JoeYun 
@Version :   1.0
@description: 批量修改文件名
'''
import os
import re
import sys
import tkinter
from tkinter import filedialog


def rename(old):
    """
        格式化文件名：1.现将扩展名分隔开；2.按照-.数字字母进行分割；3.第一个子集大写；
        4.重新组合成新的文件名
    """
    #1.获得文件扩展名
    ext = os.path.splitext(old)[1]
    #2.拆分文件名
    items = re.findall(r'[A-Za-z]+|[0-9]+', old)
    #3.获得番号数字部分
    if len(items[1]) >= 3:
        num = items[1][-3:]
    else:
        num = items[1]
    new = items[0].upper() + "-" + num + ext

    return new if not (new == old) else old


def rename_in_folder(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            os.chdir(path)
            os.rename(file, rename(file))
        else:
            rename_in_folder(file)


if __name__ == "__main__":
    print("输入文件夹路径：")
    root = tkinter.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    rename_in_folder(path)