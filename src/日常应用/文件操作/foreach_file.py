# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-02-27 18:19:06
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-03 09:06:51
@FilePath: \文件操作\foreach_file.py
@Version: 1.0
@Description:
'''

import os
import tkinter
from tkinter import filedialog

# def foreach_file_with_listdir(path):
#     count = 0
#     for file in os.listdir(path):
#         if os.path.isdir(os.path.join(path, file)):
#             foreach_file_with_listdir(os.path.join(path, file))
#         else:
#             count += 1
#     print(path.split("/")[-1] + f"文件夹下有{count}个文件！")


def foreach_file_with_walk(path):
    for root, dirs, filenames in os.walk(path):
        count = 0
        for file in filenames:
            count += 1
        print(dir + f"文件夹下有{count}个文件！")


'''
@description: 返回文件夹中文件数（只计算文件）
@param {type} 文件路径
@return: 文件数
'''


def folder_count(path):
    return len([
        name for name in os.listdir(path)
        if os.path.isfile(os.path.join(path, name))
    ])


def main():
    root = tkinter.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    print(folder_count(path))


if __name__ == '__main__':
    main()
