# on windows:
# set MYMOD=C:\Users\ivo.stoyanov\github\python\mymodule


# from mylib import fibo.fib

import sys
import os.path 
from pathlib import Path


path = os.path.expandvars("$MYMOD") 

# dunder string
path = Path(path, "mylib").__str__()
# or
#path = os.path.expandvars("$MYMOD") 
#path = f"{path}{os.path.sep}mylib"
# path = r'C:\\Users\\ivo.stoyanov\\github\\python\\mymodule\\mylib'
#print(path)

sys.path.append(path)

# print(sys.path)

from fibo import fib

fib(100)

import fibo

# print(dir(fibo))