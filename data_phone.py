import re
'''
with open('data.txt','r') as fr:
    content=fr.read()
    pattern=re.compile(r'\d{3}.\d{3}.\d{4}') #thia matches ., - as well as *
    matches=pattern.finditer(content)
    for match in matches:
        print('US phone match',match)

with open('data.txt','r') as fr:
    content=fr.read()
    pattern=re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}') #thia matches ., - only
    matches=pattern.finditer(content)
    for match in matches:
        print('US phone match',match)


with open('data.txt','r') as fr:
    content=fr.read()
    pattern=re.compile(r'\d{10}')
    matches=pattern.finditer(content)
    for match in matches:
        print('Indian phone match',match)
'''

with open('data.txt','r') as fr:
    content=fr.read()
    pattern=re.compile(r'[89]00[.-]\d{3}[.-]\d{4}') #this matches ., - only with 800 or 900 at the first 
    matches=pattern.finditer(content)
    for match in matches:
        print('US phone match',match)


