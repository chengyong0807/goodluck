#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Create by panzekai
# Create on 2019/4/19

if __name__ == '__main__':
    arr = [4,6,2,1,9,45,23]
    #反转  配合sort默认的升序效果
    #      可以实现倒序的功能
    arr.sort(reverse=True)
    for i in arr :
        print(i,end="")
        print()

    #第一象限
    for i in range(1,10) :
        for j in range(1,i+1) :
            print("%s*%s=%s"%(j,i,j*i),end="\t")
        print()

    #第二象限
    for x in range(1,10) :
        print(end= "")