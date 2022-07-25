from lib2to3.pgen2.pgen import DFAState
from types import AsyncGeneratorType
from typing_extensions import assert_type
import numpy as np
from pandas import DataFrame

i = 1
print(type(i))
while i < 6:
    print(i)
    i += 1

i = "hoi anais"
print(type(i))

i = True
print(type(i))


spielfeld = [True, False, False, True]
print(spielfeld)
print(type(spielfeld))

a = np.zeros(8)
print(a)

a = np.array(4, dtype= bool)
print(a)

a = np.zeros(4, dtype = bool)
print(a)

matrix = [[False for i in range(4)] for j in range(4)]
print(matrix)

def shw():
    print("hello")
    r = divide(2, 5) 
    print(r) 