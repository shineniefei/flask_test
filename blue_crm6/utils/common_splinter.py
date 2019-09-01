#!/usr/bin/env python3
# coding:utf-8

# pip install splinter

import os
import sys

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from splinter import Browser
from xvfbwrapper import Xvfb

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


# TODO
def splinter_xvfb():

    vdisplay = Xvfb(width=1280, height=720)
    vdisplay.start()
    print('Start...')
    browser = webdriver.Firefox()
    browser.get('http://52sox.com')
    title = browser.title
    print(title)
    print("Clean...")
    browser.close()
    vdisplay.stop()


def splinter_chrome():
    driverPath = RESPATH + "/chromedriver-2.45.exe"
    chromePath = RESPATH + "/Chrome/chrome.exe"
    # chrome_options = Options()
    options = webdriver.ChromeOptions()
    # options.add_argument("--user-data-dir=" + chromeoptionPath))
    options.add_argument("--start-maximized")
    options.add_argument("--test-type")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("allow-running-insecure-content")
    if os.path.isfile(chromePath):
        options.binary_location = chromePath

    br = Browser(
        driver_name='chrome', options=options, executable_path=driverPath)
    return br


def splinter_firefox():
    driverPath = RESPATH + "/geckodriver-0.23.0.exe"
    firefoxPath = RESPATH + "/Mozilla Firefox/firefox.exe"
    # profile = webdriver.FirefoxProfile(xx)
    # firefox_profile=profile
    if os.path.isfile(firefoxPath):
        binary = FirefoxBinary(firefoxPath)
    else:
        binary = None
    br = Browser(
        driver_name='firefox',
        executable_path=driverPath,
        firefox_binary=binary)
    return br


if __name__ == "__main__":
    browser = splinter_chrome()
    browser.visit('https://www.baidu.com')
    # browser1 = splinter_firefox()
    # browser1.visit('https://www.baidu.com')
    # browser.windows              # 获取全部窗口
    # browser.windows[0]           # 获取第一个窗口
    # browser.windows[window_name] # 获取指定窗口名的窗口
    # browser.windows.current      # 获取当前窗口
    # browser.windows.current = browser.windows[3]  # 设置当前窗口索引号为3

    # window = browser.windows[0]
    # window.is_current            # 布尔判断 - 窗口是否为当前活动窗口
    # window.is_current = True     # 设置窗口为当前窗口
    # window.next                  # 下一个窗口
    # window.prev                  # 上一个窗口
    # window.close()               # 关闭窗口
    # window.close_others()        # 关闭所有其他窗口
    # browser.reload()               # 重新加载页面
    # browser.back()
    # browser.forward()
    # browser.title
    # browser.html
    # browser.url
    # b = Browser(user_agent="Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)")
    # browser.fill('wd', '内容')
    # browser.find_by_xpath('//input[@type="submit"]').click()
    # if browser.is_text_present('splinter.readthedocs'):
    #     print "Yes, found it! :)"
    # else:
    #     print "No, didn't find it :("
    # browser.quit()
    # browser.find_by_css('h1')
    # browser.find_by_xpath('//h1')
    # browser.find_by_tag('h1')
    # browser.find_by_name('name')
    # browser.find_by_text('Hello World!')
    # browser.find_by_id('firstheader')
    # browser.find_by_value('query')
    # browser.cookies.add({'whatever': 'and ever'})
