Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import math
a=12
b=18
result =math.gcd(a,b)

print(result)
6

a=4
b=6
result =math.lcm(a,b)
print(result)
12

num=5
result=math.factorial(num)
print(result)
120


print(math.isqrt(20))
4
print(math.isqrt(50))
7

print(math.comb(4,6))
0
print(math.comb(4,2))
6
>>> print(math.perm(5,2))
20
>>> 
>>> num= 4.2
>>> print(math.ceil(num))
5

>>> num= 4.8
>>> print(math.floor(num))
4
>>> print(math.trunc(num))
4
>>> num= -25

>>> print(math.fabs(num))
25.0
>>> 
>>> result= math.fmod(10,3)
>>> print(result)
1.0
>>> result= math.modf(10.75)
>>> print(result)
(0.75, 10.0)

>>> result= math.copysign(10,-5)
>>> print(result)
-10.0
