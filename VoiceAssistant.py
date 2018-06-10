# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:27:07 2018

@author: 温一川
"""

import speech  
import win32api  
import os  
import sys  
import time  
import win32con  
command1 = {'关机': 'shutdown -s -t 1',  
             '重启': 'shutdown -r',  
             '关闭浏览器': 'taskkill /F /IM chrome.exe',  
             'google一下': 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',  
             '关闭QQ': 'taskkill /F /IM QQ.exe',  
             '关闭wifi': 'taskkill /F /IM kwifi.exe',  
             '关闭音乐': 'taskkill /F /IM cloudmusic.exe',  
             '打开音乐': 'D:\\网易云音乐\\CloudMusic\\cloudmusic.exe',  
             '放首歌': 'D:\\网易云音乐\\CloudMusic\\cloudmusic.exe',  
             '打开摄像头': 'D:\\Python源码\\摄像头监控.py',  
             '打开监控': 'D:\\Python源码\\winSpyon.py',  
             '打开QQ': 'D:\\腾讯QQ\\Bin\\QQ.exe',  
             '开启wifi': 'D:\\Chrome\\kwifi\\kwifi.exe',  
             '连接校园网': 'C:\\Drcom\\DrUpdateClient\\DrMain.exe',  
             '打开ss': 'D:\\代理服务器\\Shadowsocks-win-dotnet4.0-2.3\\Shadowsocks.exe',  
             '打开pycharm': 'D:\\PyCharm\\PyCharm 4.0.4\\bin\\pycharm64.exe',  
             '关闭pycharm': 'taskkill /F /IM pycharm.exe',  
             '打开everything': 'D:\\Chrome\\Everything\\Everything.exe',  
             '关闭everything': 'taskkill /F /IM everything.exe',  
              }  
speech.say('语音识别已开启 ')  
while True:  
    phrase = speech.input()  
    if phrase in command1.keys():  
        speech.say('即将为您%s' %phrase)  
        os.system(command1[phrase])  
        speech.say('任务已完成！')  
        if phrase == '放首歌':  
            speech.say('30秒后将播放音乐！')  
            time.sleep(35)  
            win32api.keybd_event(17, 0, 0, 0)  
            win32api.keybd_event(18, 0, 0, 0)  
            win32api.keybd_event(32, 0, 0, 0)  
            win32api.keybd_event(32, 0, win32con.KEYEVENTF_KEYUP, 0)  
            win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  
    if phrase == '退出程序':  
         speech.say('已退出程序，感谢使用！')  
         sys.exit()  