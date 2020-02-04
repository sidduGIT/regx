#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
str1='ABCDEFabcdef123450'
check=re.search(r'[^a-zA-Z0-9.]',str1)
print(check)
if check:
    print('Yes')
else:
    print('No')

#Write a Python program that matches a string that has an a followed by zero or more b's.

import re
def text_match(str1):
    if re.search(r'ab*?',str1):
        return ('found a match')
    else:
        return ('NOT found a match')
print('output is A followed by zero or more B')
print(text_match('ac'))
print(text_match('abc'))
print(text_match('abbc'))
print(text_match('bbc'))
print(text_match('bc'))

#Write a Python program that matches a string that has an a followed by one or more b's.

import re
def text_match(str1):
    if re.search(r'ab+',str1):
        return ('found a match')
    else:
        return ('NOT found a match')
print('output is A followed by 1 or more B')
print(text_match('ac'))
print(text_match('abc'))
print(text_match('abbc'))
print(text_match('bbc'))
print(text_match('bc'))

#Write a Python program that matches a string that has an a followed by two to three 'b'

import re
def text_match(str1):
    if re.search(r'ab{2,3}',str1):
        return ('found a match')
    else:
        return ('NOT found a match')
print('output is A followed by 2 to 3 B')
print(text_match('ac'))
print(text_match('abc'))
print(text_match('abbc'))
print(text_match('abbbc'))
print(text_match('bc'))

#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

def text_match(str1):

    pattern=r'^[a-z]+_[a-z]+$'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

#Write a Python program to find sequences of one upper case letter followed by lower case letters.

import re

def text_match(str1):

    pattern=r'^[A-Z]{1}[a-z]+$'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('one upper case letter followed by lower case letters')
print(text_match("cbbbc"))
print(text_match("Abbbc"))
print(text_match("Aaab"))
print(text_match("AAABCD"))
print(text_match("AAab"))

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

def text_match(str1):

    pattern=r'^a.*?b$'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('one upper case letter followed by lower case letters')
print(text_match("acbbb"))
print(text_match("abbbc"))
print(text_match("aab"))
print(text_match("AAABCD"))
print(text_match("ab"))

#Write a Python program that matches a word at the beginning of a string.

import re

def text_match(str1):
    pattern=r'^siddu+'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('start with particular word')
print(text_match("siddu acbbb"))
print(text_match("siddu santu abbbc"))
print(text_match(" siddu atharv aab"))
print(text_match("AAABCD"))
print(text_match("ab"))

#Write a Python program that matches a word at end of string, with optional punctuation.

import re

def text_match(str1):
    pattern=r'[a-z]*bagewadi$'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('end with particular word')
print(text_match("$iddu* bagewadi"))
print(text_match("siddu bagewadi "))
print(text_match("%atharv& bagewadi"))
print(text_match("AAABCD"))
print(text_match("ab"))

#Write a Python program that matches a word containing 'z'.

import re

def text_match(str1):
    pattern=r'\w+z\w+'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('containing with z')
print(text_match("sidduzbagewadi"))
print(text_match("siddu bagewadi"))
print(text_match("athzarv"))
print(text_match("AAABCDzBAGE"))
print(text_match("ab"))

#Write a Python program that matches a word containing 'z', not start or end of the word.

import re

def text_match(str1):
    pattern=r'\Bz\B'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('containing with z')
print(text_match("sidduzbagewadi"))
print(text_match("siddu bagewadi"))
print(text_match("atharvz"))
print(text_match("zAAABCDBAGE"))
print(text_match("zab"))

#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

def text_match(str1):
    pattern=r'[a-zA-Z0-9_]'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('iupper lower numbers containing')
print(text_match("sidduzbagewadi"))
print(text_match("zAAABCDBAGE"))
print(text_match("siddu bgewadi 20071980"))
print(text_match("$%%"))
print(text_match("&()*&"))

#Write a Python program where a string will start with a specific number

import re

def text_match(str1):
    pattern=r'^[0-9]+[a-zA-Z]+'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('string start with number')
print(text_match("12sidduzbagewadi"))
print(text_match("34AAABCDBAGE"))
print(text_match("siddu bgewadi"))
print(text_match("12$%%"))
print(text_match("&()*&"))

#Write a Python program where a string will start with a specific number.

import re

def text_match(str1):
    pattern=r'^5'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('string start with specific number')
print(text_match("5siddu"))
print(text_match("54AAABCDBAGE"))
print(text_match("siddu bgewadi"))
print(text_match("12$%%"))
print(text_match("&()*&"))

#Write a Python program to remove leading zeros from an IP address.

def zeros_remove(str1):
    sub_nums=str1.split('.')
    sub_nums=[int(i) for i in sub_nums]
    return '.'.join([str(i) for i in sub_nums])

print(zeros_remove('216.0.094.196'))

import re
ip='216.08.094.196'
string=re.sub('\.[0]*','.',ip)
print(string)

#Write a Python program to check for a number at the end of a string.

import re

def text_match(str1):
    pattern=r'[0-9]$'
    if re.search(pattern,str1):
        return('match found')
    else:
        return('match NOT found')
print('end  with specific number')
print(text_match("siddu5"))
print(text_match("AAABCDBAGE45"))
print(text_match("siddu bgewadi"))
print(text_match("12$%%"))
print(text_match("&()*&"))

#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

import re
str1="Exercises number 1, 12, 13, and 345 are important"
pattern=r'[0-9]{1,3}'

find=re.findall(pattern,str1)
print(find)

#Write a Python program to search some literals strings in a string. Go to the editor
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'


def text_match(str1,pat):
    if re.search(pat,str1):
        return('match found')
    else:
        return('match NOT found')
print('searching specific pattern')
str1='The quick brown fox jumps over the lazy dog.'
print(text_match(str1,'fox'))
print(text_match(str1,'dog'))
print(text_match(str1,'horse'))

#Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.

import re

pat='fox'
text='The quick brown fox jumps over the lazy dog.'
match=re.search(pat,text)
start=match.start()
end=match.end()
print('The word %s is found in %s at locations %d %d'%(pat,text,start,end))

#Write a Python program to find the substrings within a string.

str1='Python exercises, PHP exercises, C# exercises'
pat='exercises'
match=re.findall(pat,str1)
print(match)

#Write a Python program to find the occurrence and position of the substrings within a string.

import re
str1='Python exercises, PHP exercises, C# exercises'
pat='exercises'

for match in re.finditer(pat,str1):
    start=match.start()
    end=match.end()
    print('Found %s in %s at locations %d and %d'%(pat,str1,start,end))

#Write a Python program to replace whitespaces with an underscore and vice versa. 

import re

def replace(str1):
    str1=re.sub(' ','_',str1)
    return str1

print(replace('siddu bagewadi from bijapur'))

def replace(str1):
    str1=re.sub('_',' ',str1)
    return str1

print(replace('siddu_bagewadi_from_bijapur'))

import re
def replace(str1):
    if re.search(' ',str1):
        str1=re.sub(' ','_',str1)
        return str1
    elif re.search('_',str1):
        str1=re.sub('_',' ',str1)
        return str1
print(replace('Python Exercises on w3resource'))
print(replace('Python_Exercises_on_w3resource'))

#Write a Python program to extract year, month and date from an url.

import re
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

match=re.search(r'/\d{4}/\d{1,2}/\d{1,2}',url1)
print(match.group())

#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re
str1='Hi I am siddu my birthday is on 2019-10-20'
print('orig',str1)
date=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',str1)
print('modified',date)

#Write a Python program to match if two words from a list of words starting with letter 'P'.

import re
lst=['Purshan','siddu','santu','Priya','Atharv']
for i in lst:
    if re.search(r'^P[a-zA-Z]*',i):
        print(i)
for i in lst:
    if re.search(r'^s[a-zA-Z]*',i):
        print(i)

#Write a Python program to separate and print the numbers of a given string.

text = "Ten 10, Twenty 20, Thirty 30"
print(re.findall(r'\d+',text))

#Write a Python program to find all words starting with 'a' or 'e' in a given string.

str1='anand siddu santu atharv elephant surabhi emu rohini eshwar'
print(re.findall(r'\b[ae][a-zA-Z]+\b',str1))
print(re.findall(r'\b[ae]\w+\b',str1))

print(re.findall(r'\b[sa]\w+\b',str1))

#Write a Python program to separate and print the numbers and their position of a given string.

import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())

#Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

str1='this Road leads to success if you follow this Road'
str1=re.sub('Road','Rd',str1)
print(str1)

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

str1='this Road,leads to success. if you follow,this Road'
print('orig',str1)
str1=re.sub(r'[ ,.]',':',str1)
print('modified',str1)

#Write a Python program to replace maximum 4 occurrences of space, comma, or dot with a colon.

str1='this Road,leads to success. if you follow,this Road'
print('orig',str1)
str1=re.sub(r'[ ,.]',':',str1,4)
print('modified',str1)

#Write a Python program to find all five characters long word in a string.
str1='Write a Python program to find all five characters long word in a string'

print(re.findall(r'\b\w{4}\b',str1))

#Write a Python program to find all three, four, five characters long words in a string.

str1='Write a Python program to find all three, four, five characters long words in a string.'

print(re.findall(r'\b\w{3,5}\b',str1))

#Write a Python program to find all words which are at least 4 characters long in a string.

str1='Write a Python program to find all words which are at least 4 characters long in a string.'

print(re.findall(r'\b\w{4,}\b',str1))

#Write a Python program to extract values between quotation marks of a string.

str1='"Python", "PHP", "Java"'
print(re.findall(r'"[A-Za-z]+"',str1))

#Write a Python program to remove multiple spaces in a string.

str1='siddu              bagewadi'
print('orig',str1)
print('modified',re.sub(' +',' ',str1))

#Write a Python program to remove all whitespaces from a string
str1='Write a Python program to remove multiple spaces in a string.'
str1=re.sub(' ','',str1)
print(str1)

#Write a Python program to remove everything except alphanumeric characters from a string.

str1='**//Python Exercises// - 12.'
print(''.join(re.findall(r'\w+',str1))) #will contain only alphanumeric

str1='**//Python Exercises// - 12.'
print(''.join(re.findall(r'\W+',str1))) #will contain only chars

#Write a Python program to find urls in a string

str1='<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
print(re.findall(r'http[s]?://[a-z-A-Z0-9]+\.[a-z]+',str1))

#Write a Python program to split a string at uppercase letters.

str1='WriteaPythonProgramtoSplitaStringatUpperCaseletters.'
print('orig',str1)
print(re.findall('[A-Z][^A-Z]+',str1))

#Write a Python program to do a case-insensitive string replacement.

#Write a Python program to split a string with multiple delimiters.

str1='The quick: brown\nfox, jumps*over the; lazy dog.'
print('orig',str1)
print(re.split(':|\n|\*|\;|,',str1))

#Write a Python program to check a decimal with a precision of 2.

def is_decimal(num):
    dnum=re.compile(r'^[0-9]+\.[0-9]{1,2}$')
    result=dnum.search(num)
    return bool(result)

print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123'))
print(is_decimal('0.21'))

print(is_decimal('123.1214'))
print(is_decimal('3.124587'))
print(is_decimal('e666.86'))

#Write a Python program to remove words from a string of length between 1 and a given number.

str1='The quick brown fox jumps over the lazy dog.'
print('orig string',str1)
print('after removing the words from length 1 to 3')
print(re.sub(r'\b\w{1,3}\b','',str1))

#Write a Python program to remove the parenthesis area in a string.

lst=["example(.com)", "w3resource", "github(.com)", "stackoverflow(.com)"]
print('orig list',lst)
nlst=[]
for i in lst:
    new=re.sub('\(.com\)','',i)
    nlst.append(new)
print('modified list after removing (.com)',nlst)

#Write a Python program to remove lowercase substrings from a given string.

str1='write a PYTHON program TO remove LOWERCASE substrings FROM a given STRING.'
print('after removing lowercase',re.sub(r'[a-z]','',str1))
print('after removing uppercase',re.sub(r'[A-Z]','',str1))












