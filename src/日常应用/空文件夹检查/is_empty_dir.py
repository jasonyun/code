# -*- encoding: utf-8 -*-
'''
@File    :   is_empty_dir.py
@Time    :   2020/02/22
@Author  :   JoeYun 
@Version :   1.0
@Desc    :   检查公文文件夹中为空的文件夹 
'''
from os import path, listdir
from time import strftime, localtime

DEFAULT_PATH = "E:\\Dropbox\\16-天分纪检监察\\2.通知文件\\2-上级通知"


#返回路径下空文件夹名
def is_empty_dir(file_path=DEFAULT_PATH):
    with open(path.join(file_path, "result.txt"), 'w') as result:
        result.write(
            strftime("%Y-%m-%d", localtime()) + '\n' + "文件夹为空的有：" + '\n')
        for file in listdir(file_path):
            if path.isdir(path.join(file_path, file)):
                if not listdir(path.join(file_path, file)):
                    result.write(str(file) + '\n')


#返回路径下文件夹数
def folder_count(file_path=DEFAULT_PATH):
    count = 0
    with open(path.join(file_path, "result.txt"), 'a+') as result:
        for file in listdir(file_path):
            if path.isdir(path.join(file_path, file)):
                count += 1
        result.write("此路径下文件夹个数为：" + str(count) + '\n')


def main():
    path = input("请输入文件夹路径：")
    if path:
        is_empty_dir(path)
        folder_count(path)
    else:
        is_empty_dir()
        folder_count()


if __name__ == "__main__":
    main()
