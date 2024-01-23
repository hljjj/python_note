
# square function 的lambda 写法

square = lambda x: pow(x,2)

for n in range(1,11):
    print(square(n))



# lambda 和 map

m = map(lambda x: pow(x,2), list(range(1,11)))

# 第一次调用m
print(list(m))

# 第二次调用m
print(list(m))