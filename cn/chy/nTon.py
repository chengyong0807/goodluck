#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by panzekai
# Create on 2019/4/19
"""
这是
多行
注释
"""

#这是单行注释
if __name__ == '__main__':
   name = "张三"
   sex = "男"
   age =28
   #默认的输出方法
   print(name, sex, age)
   print("------")
   #替换行尾的换行,输出不换行,用end函数实现
   print(name,sex,age,end="")
   print("------")
   #参数之间去掉分隔符(一个空格),使用sep参数实现
   print(name,sex,age,sep="")
   # 参数之间变更分隔符(空格换-),添加末尾字符
   print(name, sex, age, sep="-",end="****")
   print()
   name = input("your name:")
   #使用字符串格式化输出功能
   #将format参数按照顺序填写到前面字符串的占位位置
   print("good to you {0}".format(name))
   print("你好:{0},大家热烈欢迎{0}.来为大家说说{1}".format("张三","python"))
   print("你好:{name},大家热烈欢迎{name}，{name}现在已经{age}岁了".format(name=name, age=age))
