#!/usr/bin/env python3
# coding:utf-8

import os
import sys

try:
    # 配置目录
    from conf.selenium_config import RESPATH
    if os.path.exists(RESPATH) is False:
        RESPATH = None
except Exception as e:
    RESPATH = None
finally:
    if RESPATH is None:
        RESPATH = 'D:/Test'  # 本机目录，末尾不加 “/”
    if os.path.exists(RESPATH) is False:
        print(RESPATH, ' is not find')
        sys.exit()

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def chromeDriver():
    driverPath = RESPATH + "/chromedriver-2.45.exe"
    chromePath = RESPATH + "/Chrome/chrome.exe"
    options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=" + chromeoptionPath))
    options.add_argument("--start-maximized")
    options.add_argument("--test-type")
    options.add_argument("allow-running-insecure-content")
    if os.path.isfile(chromePath):
        options.binary_location = chromePath
    dr = webdriver.Chrome(
        chrome_options=options, executable_path=driverPath, port=9976)
    print('driver started')
    return dr


def firefoxDriver():
    driverPath = RESPATH + "/geckodriver-0.23.0.exe"
    firefoxPath = RESPATH + "/Mozilla Firefox/firefox.exe"
    # profile = webdriver.FirefoxProfile(xx)
    # firefox_profile=profile
    if os.path.isfile(firefoxPath):
        binary = FirefoxBinary(firefoxPath)
        dr = webdriver.Firefox(
            executable_path=driverPath, firefox_binary=binary)
    else:
        dr = webdriver.Firefox(executable_path=driverPath)
    # 将浏览器最大化
    dr.maximize_window()
    print('driver started')
    return dr


def ieDriver():
    # 修改配置信息
    DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True
    # 获取当前文件夹的绝对路径+driver地址
    driverPath = RESPATH + "/IEDriverServer-2.53.1.exe"
    dr = webdriver.Ie(executable_path=driverPath)
    # 将浏览器最大化
    dr.maximize_window()
    # 隐性等待，最长等10秒
    dr.implicitly_wait(10)
    print('driver started')
    return dr


if __name__ == '__main__':
    # chromeDriver()
    firefoxDriver()
    # ieDriver()
