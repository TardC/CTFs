# coding: utf-8

# b  d  u   o   s   u   t   f   p   q
# 2  4  21  15  19  21  20  6   16  17
import numpy as np
import string

low = string.lowercase

key = np.matrix([[1, 1],
				 [1, 2]])

c = np.matrix([[2, 4, 21, 15, 19],
			   [21, 20, 6, 16, 17]])

p = key**-1 * c

for i in p.A1: # p.A1将二维矩阵转化为一维数组
	j = int(i) % 27 # 字母编号为 1 - 26，所以是对27取余
	print low[j-1], # low是a-z下标为 0 - 25,希尔密码为 1 - 26，所以减去1