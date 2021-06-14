import inspect


def print_var(var, context=""):
    """打印变量名及变量值"""
    name = retrieve_name(var)
    print(f"{context}{name} is {var}\n")


def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]


def descartes(x,y):
    """传入两个可迭代对象，返回笛卡尔积"""
    result = []
    for i in x:
        for j in y:
            result.append((i,j))
    return result

def getPoints(pointMax:[int,int],pointMin:[int,int],step:int):
    """给定一个矩形斜对角的两个顶点及步长,在矩形内均匀取点"""
    x = range(pointMin[0],pointMax[0],step)   
    y = range(pointMin[1],pointMax[1],step)
    points = descartes(x,y)
    return points

# points = getPoints([8,8],[4,4],1)
# print(points)