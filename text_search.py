import re
text='cat pat mat bat'
pattern=re.compile(r'[cpm]at') #match everything except bat
matches=pattern.finditer(text)
for match in matches:
    print(match)

text='cat pat mat bat'
pattern=re.compile(r'[^b]at') #match everything except bat
matches=pattern.finditer(text)
for match in matches:
    print(match)

text_name='''
        Mr.Siddu
        Ms.Sunand
        Mrs.Renuka
        Mr.Atharv
        Mrs.Raji
        '''
pattern=re.compile(r'M[rs]+\.[A-Z][a-z]+')
matches=pattern.finditer(text_name)
for match in matches:
    print(match)

text_name='''
        Mr. Siddu
        Ms Sunand
        Mrs. Renuka
        Mr Atharv
        Mrs. Raji
        '''
pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z][a-z]+')
matches=pattern.finditer(text_name)
for match in matches:
    print(match)

