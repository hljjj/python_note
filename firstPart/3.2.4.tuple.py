import pandas as pd

from common.func import print_var


path = "files/train.csv"
df = pd.read_csv(path)

#转换
col_titanic = tuple(df.columns)
record_titanic = tuple(df.values[0])

print_var(col_titanic)
print_var(record_titanic)


#属性
print(col_titanic.__contains__(1))
print(col_titanic.__len__())
print(col_titanic.count(1))