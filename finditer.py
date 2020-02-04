import re
text='abcdefghABCDEFGH'
pattern=re.compile(r'abc')
matches=pattern.finditer(text)
for match in matches:
    print(match)
print(text[0:3])

text='abcdefghABCDEFGH'
pattern=re.compile(r'DEF')
matches=pattern.finditer(text)
for match in matches:
    print(match)

print(text[11:14])
