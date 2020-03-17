# -*- coding: UTF-8 -*-

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


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('https://learnku.com/python')

    logo = (b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAtCAMAAADbYcjNAAAAAXNSR0IArs4c'
            b'6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAADBpmDFqmDBqmTFqmjJrmzJs'
            b'mzJsnDNtnTRrmjVtmjZsmzRunTRunjVvnzdwnjVwnzpxnzVwoDZxoTdyojly'
            b'oThzozhzpDh0pDp1pjp2pj51ozt3qDt4qDx4qDx5qj16qj57rD58rT98rkF1'
            b'oEB4pUB4pkR6pkJ6qEN8q0B9rUB9rkB+rkV7qUZ8qUp9p0x+p0h/rEB+sEeA'
            b'rkqArEqBr0uCrkKAsUKAskOCs0OCtESCtEWEtkaFuEaGuE2FsUiHukiIukmJ'
            b'vEmKvEqLvkuMvk2KuUyLvEyMv1OErVWDqlWHr1qHrVaIsVCMvFSPvV2LsViO'
            b'uVSQvmyUtmyXuXKbvXefv3ugv06NwE6OwFmUwl2XxGScyGmbw22hynikxnmm'
            b'yv/UO//UPP/VPf/UPv/VP//UQP/VQf/VQv/WQP/WQf/WQv/WQ//XRP/WRf/W'
            b'Sf/YRf/YRv/YR//YSP/ZSf/ZSv/aS//aTP/aTf/bTv/YUf/ZUv/bUP/cUP/c'
            b'Uv/dVP/dVv/eVv/bW//dWf/cWv/eWP/fWv/dXf/fXf/eXv/cYP/fYP/dZP/d'
            b'Zv/eZf/fZv/eaP/gW//gXP/gXv/gYP/iYf/iYv/hZP/jZP/iZv/kZv/jaf/j'
            b'a//kaP/lav/kbP/lb//mbP/mbv/ncP/mcv/iff/ocv/odP/odv/oeP/of//q'
            b'f4GnxYOox4SoxYSpx4asyo+ux4isyouuyouvzIyuyYyvy4yvzI6wy46wzIyz'
            b'0pCuyJSxyZWyy5u3zZ24zpW30pG52J250J+60aC60KS90aDC3a3E163F2K3F'
            b'2bPI2bvO3rzP3qvJ4LHN4rnR5P/qgf/qgv/qiP/sif/sjf/sj//olf/ql//u'
            b'lv/omf/qnv/tnP/qoP/ro//qpP/sov/upf/tqP/uqP/vrf/vrv/us//wpP/w'
            b'pv/xrf/wsP/wsv/ys//xtP/ytf/ytv/zuf/zuv/0vP/0vsDS38XZ6cnb6f/x'
            b'w//zwv/yxf/1w//zyP/1yf/2zP/3z//30wAAAM55ho4AAAEAdFJOU///////'
            b'////////////////////////////////////////////////////////////'
            b'////////////////////////////////////////////////////////////'
            b'////////////////////////////////////////////////////////////'
            b'////////////////////////////////////////////////////////////'
            b'////////////////////////////////////////////////////////////'
            b'/////////////////////////////////wBT9wclAAAACXBIWXMAABcQAAAX'
            b'EAEYYRHbAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAAD'
            b'nElEQVRIS62OeVhUZRSHw6IosQzGBgoIszKXqGylghKwbHErNVPbEFQQTXYo'
            b'gzZtt2SmiSEHnBHJPdM2Ldv3xbW91Pay0tT29dc53znfvTP809Pz9P7x3Xvu'
            b'8773fHvhP/M/JBce0GX/8/WduX3ipDt/1nclNrk4TnhR5y1FVzHX/KqzISY5'
            b'Uou4uLVm/sgEzF1mFqKTruozL9D8gfrM1aIwbvJaF7WFJ4FJqgtb1XOTN1R1'
            b'eBqYrLbwvpo2+SF2B/NEbFNY+IWoNum6t0UD4imgTO3CCROKiqaJqsnx8fHx'
            b'+7ho/RBALsnFxcUlJSWlNxpXkkv2I/a1uPnLWEA626WlU6aUlf3uJomJiccd'
            b'lJDAoQvFBwPsklw2deq06dNnO8nIbj3oHE4hkWDQ7HVcSzLb5eXlFRWVTtKj'
            b'+/P8OJDojfO6Wahfi3uMW1FZWVVVVV39jk2Skl6RR9JhwOjunDJUPYfZ1q6u'
            b'qampvcUmWZ4sOpcnJ9Pj8WQqHYAZ4tbW1tXV19ffbJNXPZ6sUUM8nqOBRzwe'
            b'T7LDBQDZdcYmZlz3rk2wNCUlxes9iXYcwlBmOAq4W12moeE2liXBg9QcA6yi'
            b'B+P1eqk8FtgmdoOh8SbjaoJlqacAj6ZqYqBffCJyo+GGO0S1CVYDKw8VUg0n'
            b'AJ87NnOrmk4CPJYmSNeHdjQ2Xm/kmcx9qkUlKzKU9PT0tLSTaYeVZ84i/KpF'
            b'JQ9nZmYermRknAh8qu6sOU1EUDXCJit6UuJwFu1gm+WmJp/PR7f6xr9NVE2e'
            b'OYLoaeEdVvb5/H7/XOC7QCDwoXE16d+L4IzpC3xmZLb99wYC9wPbm5mP2ZVk'
            b'RH9DP0OvK/CLcUkmmpvn0Y5gsKWlJRRykwEOXAJBI5NNBNtoRyhEJxa3bnKS'
            b'005ltBoAqGz+3E47Qq2tO9gLR+jQJAbaItdgWhdje1tbOPwHe5GFdEhyuiE7'
            b'O1sTkQ1t4fZwOBKJbCTt6/lfOsllZ0TzE9rZpV8bORKZz2z46q2ODpYlwZmC'
            b'JFfiTyuL3WHZzK4ma7QRgJ2dZcG4mmBoriEnJ4eSc4BvO9vMe0a1CQZKIwwD'
            b'dqkWxRIxnWT9QOJsITd3KN1NRRc1nQTrzs3L40y4CNitprLwbxXdBD/mM3nC'
            b'WPoQs+cBkYioBLi8oMBk+flcAHtUJ942HwwxCd4cM2hQATFO5+81WPSbfmBi'
            b'E+Cl8ZcOHvusDsBfG+hKm/foJHRO/hXgH831bVAP1oP5AAAAAElFTkSuQmCC')

    menu_def = ['My_Menu', ['Start', 'Quit']]
    tray = sg.SystemTray(menu=menu_def, data_base64=logo)

    flag = False
    while True:

        event = tray.read(timeout=300000)
        print(event)

        if event in [None, 'Quit']:
            break

        if flag:
            try:
                driver.refresh()  # 刷新页面
                notify()  # 讯息通知
            except:
                pass
        else:
            if event == 'Start':
                # 寻找所有的窗口, 比对标题内容, 决定是否隐藏窗口
                win32gui.EnumWindows(enumWindowFunc, [])
                notify()
                flag = True

    driver.close()
    driver.quit()
    tray.close()
