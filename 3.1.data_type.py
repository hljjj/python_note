from common.func import print_var

# python的基本数据类型

# 字符串
words = "hello,world"
print_var(words)

# 整型
type_int = 20201111
print_var(type_int)

# 浮点数
type_float = 3.14158
print_var(type_float)

# 复数 实数+虚数
type_complex1 = 1+2j
type_complex2 = complex(1,2)
print_var(type_complex1)
print_var(type_complex2)

# 布尔值
type_bool_1 = True
type_bool_0 = False
print_var(type_bool_1)
print_var(type_bool_0)

# 列表
iPhone = ['iphon6', 'iphone6s', 'iphone SE', 'iphone7', 'iphone8', 'iphoneX', "iphone11"]
print_var(iPhone)

# 元组
color = ('blue', 'black', 'white', 'green', 'red')
print_var(color)

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
print_var(iphone12)

