import re
text='atharv bagewadi 123-456-7891 siddu bagewadi 123.456.7891'
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern=re.compile(r'\d{3}-|.\d{3}-|.\d{4}')
matches=pattern.findall(text)
print(matches)
'''if matches:
    print('matched')
else:
    print('not matched')'''

text='atharv bagewadi 123-456-7891 siddu bagewadi 123.456.7891'
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
matches=pattern.finditer(text)

for match in matches:
    print(match)

print(text[16:28])
print(text[44:56])

