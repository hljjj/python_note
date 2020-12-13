
# extract the English words from ass file

# read the file
path = "files"
filename = "The.Social.Dilemma.ass"

with open(f"{path}/{filename}", "r", encoding="utf-8") as f:
    words = f.readlines()

# find the start index of "Dialogue" 
first_word = ""
for i in words:
    if i.find("Dialogue") != -1:
        first_word = i
        break

start = words.index(first_word)

# format and extract
words = words[start:]     
english = []

# find the start of english word
for i in words:
    start = i.rfind("}")+1
    english.append(i[start:])

# output
output_file = "file/words.txt"
with open(output_file, "a", encoding="utf-8") as f:
    for i in english:
        f.writelines(i)

print(f"{output_file} is done")

# improve: import re to delete chinese 
