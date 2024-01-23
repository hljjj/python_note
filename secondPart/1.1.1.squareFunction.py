
# 定义函数

def square(baseNumber):
    """传入底数，打印底数平方的式子及结果"""
    squareN = pow(baseNumber,2)
    print(f"{baseNumber}*{baseNumber}={squareN}")


square(1)
square(2)
square(3)
square(4)
square(5)
square(6)
square(7)
square(8)
square(9)
square(10)

print("\nfor的写法")

for n in range(1,11):
    square(n)


    