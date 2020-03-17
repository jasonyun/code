# -*- encoding: utf-8 -*-
'''
@File    :   xiami_checkin.py
@Time    :   2020/02/20
@Author  :   JoeYun 
@Version :   1.0
@description: 每天自动登录虾米签到
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import schedule
import time
import os

USERNAME = "18103119100"
PASSWORD = "20040719"


def login_xiami():
    url = 'https://www.xiami.com/'

    option = webdriver.ChromeOptions()
    #隐藏信息栏
    option.add_argument('--disable-infobars')
    #窗口最大化
    option.add_argument('--start-maximized')
    option.add_argument(
        'user-agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"'
    )
    option.add_argument('--disable-extensions')
    option.add_argument('--profile-directory=Default')
    option.add_argument("--incognito")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path="chromedriver.exe",
                              options=option)
    driver.get(url)
    try:
        time.sleep(2)
        driver.implicitly_wait(20)
        time.sleep(0.1)
        #隐藏webdriver
        driver.execute_script(
            'Object.defineProperties(navigator,{webdriver:{get:()=>false}})')

        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div/div[3]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="passport-form"]/div[2]/div/div[1]/span[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="account"]').send_keys(USERNAME)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
        #找到滑块元素
        element = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        #按住不放
        ActionChains(driver).click_and_hold(on_element=element).perform()
        time.sleep(0.5)
        #移动指定距离 滑动条尺寸为280*34,滑块尺寸为40*34
        ActionChains(driver).move_to_element_with_offset(element, 240,
                                                         0).perform()

        for track in [2, 4, 6, 9]:
            #分段移动指定距离
            ActionChains(driver).move_by_offset(track, 0).perform()
            time.sleep(0.8)
        #释放鼠标
        ActionChains(driver).release().perform()
        time.sleep(2)
        #点击登录
        driver.find_element_by_xpath('//*[@id="account-login-submit"]').click()
        time.sleep(6)
        print("登录成功！")
    finally:
        driver.close()


if __name__ == "__main__":
    # schedule.every(10).minutes.do(login_xiami)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    login_xiami()