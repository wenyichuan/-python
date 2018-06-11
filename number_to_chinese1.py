# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 17:20:17 2018

@author: 温一川
"""

unitArab=(2,3,4,5,9)
unitStr=u'十百千万亿'
unitStr=u'拾佰仟万亿'
#单位字典unitDic,例如(2,'十')表示给定的字符是两位数,那么返回的结果里面定会包含'十'.3,4,5,9以此类推.
unitDic=dict(zip(unitArab,unitStr))

numArab=u'0123456789'
numStr=u'零一二三四五六七八九'
numStr=u'零壹贰叁肆伍陆柒捌玖'
#数值字典numDic,和阿拉伯数字是简单的一一对应关系
numDic=dict(zip(numArab,numStr))


def ChnNumber(s):
    def wrapper(v):
        '''针对多位连续0的简写规则设计的函数
        例如"壹佰零零"会变为"壹佰","壹仟零零壹"会变为"壹仟零壹"
        '''
        if u'零零' in v:
            return wrapper(v.replace(u'零零',u'零'))
        return v[:-1] if v[-1]==u'零' else v
    def recur(s,bit):
        '''此函数接收2个参数:
        1.纯数字字符串
        2.此字符串的长度,相当于位数'''
        #如果是一位数,则直接按numDic返回对应汉字
        if bit==1:
            return numDic[s]
        #否则,且第一个字符是0,那么省略"单位"字符,返回"零"和剩余字符的递归字符串
        if s[0]==u'0':
            return wrapper(u'%s%s' % (u'零',recur(s[1:],bit-1)))
        #否则,如果是2,3,4,5,9位数,那么返回最高位数的字符串"数值"+"单位"+"剩余字符的递归字符串"
        if bit<6 or bit==9:
            return wrapper(u'%s%s%s' % (numDic[s[0]],unitDic[bit],recur(s[1:],bit-1)))
        #否则,如果是6,7,8位数,那么用"万"将字符串从万位数划分为2个部分.
        #例如123456就变成:12+"万"+3456,再对两个部分进行递归.
        if bit<9:
            return u'%s%s%s' % (recur(s[:-4],bit-4),u"万",recur(s[-4:],4))
        #否则(即10位数及以上),用"亿"仿照上面的做法进行划分.
        if bit>9:
            return u'%s%s%s' % (recur(s[:-8],bit-8),u"亿",recur(s[-8:],8))
    return recur(s,len(s))

while True:
    p = input("请输入数字：")
    print(ChnNumber(p))
    
    
