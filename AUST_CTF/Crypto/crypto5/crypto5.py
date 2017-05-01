# coding: utf-8

e = 17
n = 568897489
c = [
	316594585, 
	45808437, 
	229743105, 
	194984426, 
	372147352, 
	246402026, 
	500264009, 
	372147352, 
	45808437, 
	14911488
]
m = []

for i in xrange(2, n): # RSA中 n = p * q, 且p和q均为素数，求得p后, q = n / p
	if n % i == 0:
		p = i
		break
		pass

q = n / p

def ext_euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_euclid(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def get_inverse(a, b): # 利用扩展欧几里得算法求解密密钥d
    x, y, q = ext_euclid(a, b)
    if x < 0:
        x = (x + b) % b
    return x

r = (p-1)*(q-1)
d = get_inverse(e, r)

for i in c: # 求得明文为[106L, 117L, 115L, 116L, 102L, 111L, 114L, 102L, 117L, 110L]
	m.append(pow(i, d, n))

for i in m: # 明文为ASCII码, 转换为字母
	print chr(i), 