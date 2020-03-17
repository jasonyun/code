# -*- encoding: utf-8 -*-
'''
@File    :   create_folder.py
@Time    :   2020/02/12 21:22:46
@description:新建文件夹方法 
@Author  :   JoeYun 
@Version :   1.0
'''

import os


def create_folder(path, name):
    # 创建文件夹
    folder_path = os.path.join(path, name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


if __name__ == '__main__':
    create_folder(os.path.dirname(__file__), "new_folder")
