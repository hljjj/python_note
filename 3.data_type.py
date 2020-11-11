
# python的基本数据类型

# 字符串
words = "hello,world"
print(f"words is {type(words)}\n")

# 整型
type_int = 20201111
print(f"type_int is {type(type_int)}\n")

# 浮点数
type_float = 3.14158
print(f"type_float is {type(type_float)}\n")

# 复数 实数+虚数
type_complex1 = 1+2j
type_complex2 = complex(1,2)
print(f"type_complex1 is {type(type_complex1)}\n")
print(f"type_complex2 is {type(type_complex2)}\n")


# 布尔值
type_bool_1 = True
type_bool_0 = False
print(f"type_bool_1 is {type(type_bool_1)}\n")
print(f"type_bool_0 is {type(type_bool_0)}\n")

# 列表
iPhone = ['iphon6', 'iphone6s', 'iphone SE', 'iphone7', 'iphone8', 'iphoneX', "iphone11"]
print(f"iPhone is {type(iPhone)}\n")

# 元组
color = ('blue', 'black', 'white', 'green', 'red')
print(f"color is {type(color)}\n")

# 字典
iphone12 = {
    'name': 'iphone12',
    'touch_id': 0,
    'face_id': 1,
    'display':'6.1‑inch',
    'weight': '164 grams',
    'capacity': ('64GB', '128GB', '256GB'),
    'price': (699, 749, 849)
}
print(f"iphone12 is {type(iphone12)}\n")

