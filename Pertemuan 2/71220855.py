
# import timeit

# mulai=timeit.default_timer()
# nilai=0
# for i in range(10000):
#     nilai=nilai+1*2
# akir=timeit.default_timer()
# print(akir-mulai)


# def head_recursion(n):
#     if n==0:
#         return
#     else:
#         head_recursion(n-1)
#     print(n)

# head_recursion(10000)

# import sys


# def tail_recursion(n):
#     if n==0:
#         return
#     else:
#         print(n)
#     tail_recursion(n-1)

# tail_recursion(10000)

import random
import timeit

def generate_list(n):
    batas_atas=n*100
    randomlist=random.sample(range(0, batas_atas),n)
    randomlist.sort()
    return randomlist

def cari_pasangan(data, target):
    for i in range(0, len(data)-1):
        for j in range(i, len(data)):
            if data[i]+data[j]== target:
                print(data[i], "+", data[j], "=", target)
                return True
        return False
    

for i in range(5000, 55000, 5000):
    data=generate_list(i)
    target=-100
    start=timeit.default_timer()
    hasil=cari_pasangan(data, target)
    end=timeit.default_timer()

    print(f"x {i} : {end-start} second")



# import random

# def genrate_list(n):
#     batas_atas=n*100
#     randomlist=random.sample(range(0, batas_atas),n)
#     randomlist.sort()
#     return randomlist
# print(genrate_list(100))