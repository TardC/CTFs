# coding: utf-8

import string

lowercase = string.lowercase
str1 = 'hfjxfwnxxnruqj'
str2 = ''

for i in xrange(0, 26): # 移位位数为1,2,3,...25
	for j in str1:
		str2 += lowercase[(lowercase.index(j)+i)%26]
	print str2
	str2 = ''

