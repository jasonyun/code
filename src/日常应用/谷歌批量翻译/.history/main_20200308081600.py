# -*- coding: UTF-8 -*-
'''
@Author: Joe.Yun
@Date: 2020-02-24 21:41:19
@LastEditors: Joe.Yun
@LastEditTime: 2020-03-08 08:15:59
@FilePath: \谷歌批量翻译\main.py
@Version: 1.0
@Description: 
 
'''

from os import path, listdir
from GoogleTranslator import GoogleTranslator
from time import time
from xlrd import open_workbook
from re import sub
from tkinter import Tk, filedialog
'''
@description: 
@param {type} 
@return: 
'''


def readFile(fileName):
    with open(fileName, 'r', encoding="gb18030", errors="ignore") as f:
        paragraph = ''
        for line in f:
            if line[0] != '\n':
                paragraph += line.strip('\n')
            else:
                if len(paragraph) > 0:
                    yield paragraph
                    paragraph = ''
        if len(paragraph) > 0:
            yield paragraph


'''
@description: 
@param {type} 
@return: 
'''


def get_word_from_xls(xls_file):
    data = open_workbook(xls_file, encoding_override="gb18030")
    table = data.sheets()[0]
    with open(xls_file.split(".")[0] + ".txt", 'w',
              encoding="gb18030") as data:
        for i in range(1, table.nrows):
            data.write("<" + table.cell(i, 0).value + ">" + "\n")
            #删除版权信息
            input_word = sub(u"COPYRIGHT:|amp;|&lt;|P&gt;|&gt;", "",
                             table.cell(i, 11).value)
            data.write(input_word + "\n\r")
        print("已将%s文件摘要部分保存至txt" % xls_file.split("//")[-1])


def translate_from_file(file):
    startTime = time()
    translator = GoogleTranslator()
    count = 0
    with open(file.split(".")[0] + "-翻译版.txt", 'w', encoding="utf-8") as df:
        for line in readFile(file):
            if len(line) > 1:
                count += 1
                print('\r' + str(count), end='', flush=True)
                df.write(line.strip() + "\n")
                result = translator.translate(line)
                df.write(result.strip() + "\n\n")
                print("篇已翻译完成！")
    print(file.split("\\")[-1] + '已翻译完成，用时%.2f 秒' % (time.time() - startTime))


#输入装有*.xls文件的文件夹路径workpath[0]，输出翻译好的txt文件
def main():
    print("请选择待翻译文件夹：（注意放在文件夹下后选择此文件夹！）")
    root = Tk()
    root.withdraw()
    file_path = filedialog.askdirectory()
    if path.isdir(file_path):
        for xls_file in listdir(file_path):
            #从xls文件中提取出摘要到txt
            get_word_from_xls(path.join(file_path, xls_file))
            #逐个进行翻译
            translate_from_file(
                path.join(file_path,
                          xls_file.split(".")[0] + ".txt"))
        print("翻译工作完成，请查看文件夹")


if __name__ == "__main__":
    main()