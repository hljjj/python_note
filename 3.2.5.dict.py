from common.func import print_var



# 创建新字典
agent_1 = { 'name': 'Daisy'}
agent_2 = { 'name': 'Coulson',
            'level': 8,
            'position': 'Director',
            'intelligence': 160,
            'strength': 100,
            'ability': 'resurrection'}
print_var(agent_1)

# 返回值
# python没有同名key
same_key = {'name': 'Daisy', 'name': 'Sky'}

# 字典的属性
agent_2.__len__()
agent_2.keys()
agent_2.values()
agent_2.items()


# 字典的增删改

# 删
print_var(agent_2)
del agent_2['strength'] # 删除指定的k,v
print_var(agent_2, 'after del strength ')
agent_2.pop('ability')  # 弹出指定k,v
print_var(agent_2, 'after pop ability ')
agent_2.popitem()  # 弹出最后一个输入的k,v
print_var(agent_2, 'after popitem ')

# 增
agent_2['strength'] = 100
agent_2['ability'] = 'resurrection'
agent_2['intelligence'] = 160
print_var(agent_2, 'after adding key ')

# 改
same_key = {'name': 'Daisy'}
print_var(same_key)
same_key['name'] = 'Sky'
print_var(same_key, "atfer modify ")
