import re

m=re.match(r'(\w+)@(\w+)\.(\w+)','bagewadi@gmail.com')

print(m.group(0))   #entire match 
print(m.group(1))   #the first paranthesis
print(m.group(2))   #the second paranthesis
print(m.group(3))   #the third paranthesis

print(m.groups())   #return entire subgroups matching as tuple
