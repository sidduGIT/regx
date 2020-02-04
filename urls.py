import re

urls='''
https://www.google.com
http://coreymschafer.com
https://youtube.com
https://www.nasa.gov
http://coreyms.com
'''

pattern=re.compile(r'(http|https)://[a-z.]+\.[a-z]+')
matches=pattern.finditer(urls)
for match in matches:
    print(match)

pattern=re.compile(r'(https?)://(www\.)?[a-z]+\.[a-z]+')
matches=pattern.finditer(urls)
for match in matches:
    print(match)

