import re
str1='abcd11gjgjgj789fjfjflj10jffjf34fkfkf45'

find=re.findall(r'[0-9]+',str1)
print(find)

str1='siddu bagewadi 9880890865 bijapur'
print(re.findall(r'[0-9]+',str1))
