from common.func import print_var

#新建一个空列表
list_a = []
print_var(list_a)

#1.改变list本身

#增加
list_b = [1,2,3]
print_var(list_b)
list_a.append(list_b)
print_var(list_a, "after append list_b, ")
list_a.extend(list_b)
print_var(list_a, "after extend list_b, ")
list_a.insert(2, list_b)
print_var(list_a, "after insert list_b before index 2, ")

#删除
del list_a[2]
print_var(list_a, "after delete index of 2, ")
del list_a[0:2]
print_var(list_a, "after delete index of 0 : 2, ")
pop = list_a.pop(0)
print_var(pop, "pop the index of 0, ")
print_var(list_a, "after pop, ")
list_a.remove(3)
print_var(list_a, "after remove 3, ")

#修改
list_a.append(list_b)
list_a.extend(list_b)
list_a.insert(2, list_b)
list_c = [1,2,3,'apple','pear',4,5,'orange']
list_d = [1,3,5,7,9,2,4,6,8]
list_e = ['apple','bear','class','decode','11','12','1','apache']
list_f = [[3,4,1],[9,2,7],[5,6,8,7,10]]
print_var(list_a, "\nnew list\n")
print_var(list_c)
print_var(list_d)
print_var(list_e)
print_var(list_f)

#排序
#sort只能用于同类型数据中，reverse只是单纯地反转
list_d.sort()
print_var(list_d, "after sort, ")
list_e.sort(reverse=True)
print_var(list_e, "after sort by desc, ")
list_f.sort()
print_var(list_f, "after sort, ")
list_c.reverse()
print_var(list_c, "after reverse, ")

#修改
list_c[0]='1'
print_var(list_c, "after change index 0 to value 1,")
list_c[1:3]='1:3'
print_var(list_c, "after change [1:3] to '1:3', ")
list_c[1:3] = list_f
print_var(list_c, "after change [1:3] to list_f, ")

# 用list_d扩展list_c，从第二个位置开始
# 切片,1:1是从1开始，在1结束，不会替换原来的值，但":"是必不可少的
list_c[1:1] = list_d
print_var(list_c, "after slice 1:1 to extend, ")


#2.返回新的对象
slicing = list_c[:9]
to_str = str(list_c)
to_tup = tuple(list_c)
to_list = list('hey')
copy_list = list_c.copy()
print_var(slicing)
print_var(to_str)
print_var(to_tup)
print_var(to_list)
print_var(copy_list)


print('\n')
#3.获取list的属性
# 判断是否存在某个值
print(f"whether contains value of 1, {list_c.__contains__(1)}")
# 统计某个值的个数
print(f'count of 1, {list_c.count(1)}')
# 获取list的长度
print(f"length of list_c,{list_c.__len__()}")


# tips 如非必要，不要直接把一个变量赋值给另一个变量


