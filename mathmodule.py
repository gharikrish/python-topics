Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> x = 5.4
>>> # floor()
>>> print(math.floor(x))
5
>>> 
>>> #ceil(max int value)
>>> 
>>> print(x)
5.4
>>> print(math.ceil(x))
6
>>> #factorial
>>> print(math.factorial(3))
6
>>> #gcd
>>> print(math.gcd(4,4))
4
>>> print(math.gcd(2,6,12))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(math.gcd(2,6,12))
TypeError: gcd expected 2 arguments, got 3
>>> print(math.gcd(24,78))
6
>>> #sqrt
>>> print(math.sqrt(25))
5.0
>>> print(math.isqrt(25))
5
>>> #exponential
>>> #e^val
>>> print(math.exp(6))
403.4287934927351
>>> 
>>> #module
>>> print(math.fmod(10,3))#x>y reminder
1.0
>>> print(math.fmod(3,10)) #x<y
3.0
>>> #copysign
>>> x= 5
>>> y= -6
>>> print(math.copysign(x,y))
-5.0
>>> 
>>> #difference
>>> print(3-7)
-4
>>> #fabs
>>> print(math.fabs(x,y))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(math.fabs(x,y))
TypeError: fabs() takes exactly one argument (2 given)
>>> print(math.fabs(x-y))
11.0
>>> x=4
>>> y=5
>>> print(math.fabs(x-y))
1.0
>>> #power
>>> print(math.pow(2,6))
64.0
>>> #list accesss in math module
>>> #fsum
>>> lst = [1,2,3,4,5,6,7,7]
>>> print(math.fsum(lst))
35.0
>>> #product
>>> print(math.prod(lst))
35280
>>> print(math.sin(0))
0.0
>>> print(math.sin(1))
0.8414709848078965
>>> print(math.cos(90))
-0.4480736161291701
>>> #constant
>>> print(math.pi)
3.141592653589793
>>> print(math.tau)
6.283185307179586
>>> print(mat.e)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(mat.e)
NameError: name 'mat' is not defined
>>> print(math.e)
2.718281828459045
>>> print(math.nan)
nan
>>> print(math.inf)
inf
>>> #condition check
>>> #constant implement
>>> x = 10
>>> print(math.isfinite(x))
True
>>> print(math.isinf(x))
False
>>> print(math.isnan(x))
False
>>> #math.isclose
>>> print(math.isclose(1.1,1.2))
False
>>> print(math.isclose(1.1,1.2,tol=0.2))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(math.isclose(1.1,1.2,tol=0.2))
TypeError: 'tol' is an invalid keyword argument for isclose()
>>> 
>>> print(math.isclose(1.1,1.2,abs_tol=0.2))
True
>>> print(math.isclose(1.1,1.3,abs_tol=0.2))
True
>>> 