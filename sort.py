
from tkinter import VERTICAL


data = {"SG":20, "AA":40, "BB":90}

sortDict = {}

for i in sorted(list(data.keys())):
    sortDict[i] = data[i]
    
    
for k,v in sortDict.items():
    print(k,v)

