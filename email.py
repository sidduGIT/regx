import re

str1='hi how are you 123siddu-bagewadi1978@gmail.com i am waiting for your input on this'

find=re.findall(r'[a-zA-Z0-9._-]+\@+[a-zA-Z0-9.]+',str1)
print(find)

emails='''
siddu.bagewadi@gmail.com
SidduMbagewadi@university.edu
siddu-321-bagewadi@my-work.net
'''
pattern=re.compile(r'[a-zA-Z00-9.-]+@[a-zA-Z-]+\.[a-z]+')
matches=pattern.finditer(emails)
for match in matches:
    print(match)

emails='''
siddu1978@gmail.com
siddu.bagewadi@yahoo.co.in
'''
pattern=re.compile(r'[a-z0-9.]+@[a-z]+(\.com|\.co.in)')
matches=pattern.finditer(emails)
for match in matches:
    print(match)
