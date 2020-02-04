import re

text='siddu bagewadi Atharv1 bagewadi atharv surabhi bagewadi'
pattern=re.compile(r'siddu')
matches=pattern.match(text)
print(matches)

pattern=re.compile(r'atharv')
matches=pattern.search(text)
print(matches)
