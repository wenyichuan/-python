# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 10:32:12 2018

@author: 温一川
"""
import pygame

def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open("unicode_py.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for i in x:
        i = str(i.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
        except:
            y += 'XXXX '#表示非法字符
    return y

def make_voice(x):
    pygame.mixer.init(frequency = 22050,size = -16,channels = 2,buffer = 4096)
#初始化混音器模块以进行声音加载和播放。默认参数可以被覆盖以提供特定的音频混合。关键字参数被接受。为了后向兼容性，将参数设置为零，使用默认值（可能会通过pre_init调用进行更改）。
#size参数表示每个音频采样有多少位。如果该值为负值，则将使用带符号的采样值。正值表示将使用未签名的音频采样。无效值引发异常。
#通道参数用于指定是使用单声道还是立体声。1为单声道，2为立体声。没有其他值被支持（负值被视为1，大于2的值被视为2）。
#缓冲区参数控制混音器中使用的内部采样的数量。默认值应该适用于大多数情况。它可以降低以减少延迟，但可能发生声音丢失。可以将其提高到更大值以确保播放不会跳过，但会对声音播放造成延迟。缓冲区大小必须是2的幂（如果不是，则将其舍入到下一个最接近的2的幂）。
    voi = chinese_to_pinyin(x).split()
    for i in voi:
        if i == 'XXXX':#对于非法字符将其跳过
            continue
        pygame.mixer.music.load( "voice/"+i.lower() + ".wav")
#这将加载音乐文件名/文件对象并准备播放。如果音乐流正在播放，则会停止播放。这不会启动音乐播放。
        pygame.mixer.music.play()
#这将播放加载的音乐流。如果音乐已经播放，它将被重新启动。
        while pygame.mixer.music.get_busy() == True:
#当音乐流正在播放时返回True。当音乐闲置时，返回False。
            pass
    return None

while True:
    p = input("请输入文字：")
    make_voice(p)
    