
func = """'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 
'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 
'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 
'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 
'tuple', 'type', 'vars', 'zip'"""


#IO
print(" print 在屏幕上打印字符串")

inputVal = input("请输入内容:")
print(f"input 接受控制台输入,刚刚输入的内容是 {inputVal}")

path = "files/HelloWorld.txt"

openObj = open(path,"w")  # w为覆盖模式，要求文件事先存在，a为追加，不存在会新建
openObj.write(inputVal)
openObj.close()
print(f"已将输入内容输出为文件，输入内容:{inputVal}，路径：{path}")

#算术运算

#集合操作
listSort = [3,5,6,1,12]
print(sorted(listSort))
print(reversed(listSort))

#类操作
class Employee():

    def __init__(self,name="NoName",age=25,salary=10000,posititon="SDE"):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = posititon

    def logInfo(self):
        print(f"name is {self.name}\nage is {self.age}\nsalary is {self.salary}")

    @classmethod
    def introduce(self):
        print("员工类，调用以创建员工对象\n输入属性：\n姓名\n年龄\n薪资\n岗位")

# 在未加 classmethod 之前，不能直接调用类的方法，会报错，此时self是必须的
Employee.introduce()

# 没有classmethod只能通过创建对象的方式调用
cassie = Employee('cassie')
cassie.introduce()

# 注意，就是加了classmethod，也需要原始代码里支持这种用法，如果原始代码涉及到对象的调用，仍然会报错
cassie.logInfo()
try:
    Employee.logInfo()
except Exception as e:
    print(f"类引用报错，{e}")
