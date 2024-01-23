import random


food_list = ['鸡腿', '牛肉', '羊肉']
# 从foot_list随机抽取一种食材
food = random.sample(food_list, 1)[0]
# randint输入的参数是一个闭区间
time = random.randint(10,120)
# 菜单
print(f'随机生成食材:{food}\n烹饪时长:{time}\n')
if food == '鸡腿':
    if time < 30:
        print('夹生的鸡腿')
    # 烹饪30-40分钟的香酥鸡腿
    elif time >= 30 and time <= 40:
        print('香酥鸡腿')
    elif time > 40 and time <= 60:
        print('烤糊的鸡腿')
    else:
        print('烧成炭的鸡腿')
elif food == '羊肉':
    if time < 40:
        print('夹生的羊肉')
    elif time >= 40 and time <= 50:
        print('碳烤羊肉')
    elif time > 50 and time <= 70:
        print('烤糊的羊肉')
    else:
        print('化成灰的羊肉')
elif food == '牛肉':
    if time < 40:
        print('夹生的牛肉')
    elif time >= 40 and time <= 50:
        print('碳烤牛肉')
    elif time > 50 and time <= 70:
        print('烤糊的牛肉')
    else:
        print('不能吃的牛肉')
else:
    print('未知菜谱')