
# 新建一个字符串
words = "hello,world"

# 长字符串
context = """
Never give up,
Never lose hope.
Always have faith,
It allows you to cope.
Trying times will pass,
As they always do.
Just have patience,
Your dreams will come true.
So put on a smile,
You'll live through your pain.
Know it will pass,
And strength you will gain
"""
print(context)

# 索引访问元素
hello = words[:5]

# 字符串拼接
new_words_1 = "hello"+",python"
new_words_2 = "hello,{},{}".format('python','nice to meet you')
new_words_3 = "hello,{1},{0}".format('python','nice to meet you')
new_words_4 = ".".join(["ab","cd","ef"])



# fromat的简写
name = input("请输入名字:")
welcome = f"hello,{name}"
print(welcome)


# 字符串的修改
upper = words.upper()
lower = upper.lower()

# 返回单词开头大写的英文字符
words.title()

# str.replace(old,new)
words.replace("world","python")

# strip 清除首尾空格
trip_string = '  string    '
print(trip_string.strip())

# lstrip 清除左边空格 left strip
# rstrip同理，right strip
print(trip_string.lstrip())

# 对字符串进行拆分
split_1 = new_words_3.split(',')
split_2 = new_words_3.split()

# 判断字符是否字母、数字、大写、小写，都是返回bool值
"hello".isalpha()
"2020".isdigit()
words.isupper()
words.islower()

# find 会返回第一次出现匹配字符串的位置索引
words.find("w")



