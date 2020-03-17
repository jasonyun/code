# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-03-04 14:57:28
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-04 15:18:20
@FilePath: \文件操作\add_folder.py
@Version: 1.0
@Description: 批量建立各单位文件夹
'''
from os.path import join, exists
from os import makedirs
'''
@description: 从dw_list.txt中逐行读取单位名称，并建立文件夹
@param {type} root_path
@return: 
'''


def add_folder(root_path):
    for name in open('dw_list.txt', encoding='utf-8'):
        folder_path = join(root_path, name.strip('\n'))
        if not exists(folder_path):
            makedirs(folder_path)
        else:
            print("文件夹已存在")


def main():
    root = input("请输入要创建文件夹的路径: ")
    add_folder(root)

if __name__ == '__main__':
    main()
