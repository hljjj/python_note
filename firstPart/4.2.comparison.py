import random
from common.func import print_var

# randint(a,b)返回range(a,b)的随机整数,区间是[a,b)
# 懒得造数据的时候，可以用random模块随机生成
def rand_num():
    """返回一个[0,100]的随机整数"""
    num = random.randint(0,101)
    return num


a = 10
b = 15
if a <= b: 
    if a == b: 
        print("a is equal to b")
    else:  
        print("a is less then b")
else: 
    print("a is greater than b")



