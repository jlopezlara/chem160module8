Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> N=1000
>>> m3=np.arange(0,N,3)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    m3=np.arange(0,N,3)
NameError: name 'np' is not defined
>>> m5=np.arange(0,N,5)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    m5=np.arange(0,N,5)
NameError: name 'np' is not defined
>>> m35=np.concatenate([m3,m5])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    m35=np.concatenate([m3,m5])
NameError: name 'np' is not defined
>>> m35u=np.unique(m35)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    m35u=np.unique(m35)
NameError: name 'np' is not defined
>>> print("Sum of 3 and 5 multiples below %d is %d"%(N,m35u.sum()))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("Sum of 3 and 5 multiples below %d is %d"%(N,m35u.sum()))
NameError: name 'm35u' is not defined
>>> 
