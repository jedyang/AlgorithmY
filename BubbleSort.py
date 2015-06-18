#coding=utf-8
import random 

""" 
冒泡排序最基础的版本. 
顺序比较相邻元素
 """

def bubbleSort(srcAry): 
	n = len(srcAry) 
	for i in range(1, n): 
		for j in range(n-i): 
			if srcAry[j] > srcAry[j+1]: 
				srcAry[j], srcAry[j+1] = srcAry[j+1], srcAry[j] 
	return srcAry

""" 
冒泡排序改进1 
增加一个变量记录最后一次交换的位置 
该位置之后都是排好序的 
""" 

def bubbleSort1(srcAry): 
	n = len(srcAry) 
	seg = n - 1 
	for i in range(1, n): 
		for j in range(seg): 
			if srcAry[j] > srcAry[j+1]: 
				srcAry[j], srcAry[j+1] = srcAry[j+1], srcAry[j] 
				seg = j 
	return srcAry

""" 
冒泡排序改进2 
再增加一个变量记录是否有位置交换 
如果某趟排序没有位置交换 
说明已经排好序，可以退出。 
""" 

def bubbleSort2(srcAry): 
	n = len(srcAry) 
	seg = n - 1 
	for i in range(1, n): 
		flag = 1 
		for j in range(seg): 
			if srcAry[j] > srcAry[j+1]: 
				srcAry[j], srcAry[j+1] = srcAry[j+1], srcAry[j] 
				seg = j 
				flag = 0 
			if flag: 
				return srcAry 
	return srcAry


if name == "main": 
	ary = [random.randint(1, 99) for i in range(20)] 
	print("ss")
	print "ssss"
	print("before:" + str(ary)) 
	print("after:" + str(bubbleSort2(ary)))