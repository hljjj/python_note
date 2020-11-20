
import decimal
import math

from common.func import print_var

# 高精度的小数计算，默认精度28位
prec28 = decimal.Decimal(10)/3
print_var(prec28)

# 修改精度=64，精确到小数点后63位
decimal.getcontext().prec = 64

prec64 = decimal.Decimal(10)/3
print_var(prec64)

# math
# 三角函数
π = math.pi
cos = math.cos(π)
sin = math.sin(π/2)
print_var(cos)
print_var(sin)

# 对数
e = math.e
log = math.log(2**8,2)
log10 = math.log10(10**3)
log1p = math.log1p(e**4)
print_var(log)
print_var(log10)
print_var(log1p)


