

def findoccurence(str1,substr):
    count=0
    start=0
    while start<len(str1):
        flag=str1.find(substr,start)

        if flag!=-1:
            start=flag+1
            count+=1
        else:
            return count

print(findoccurence('geeksforgeeksforgeeksforgeeks','geeksforgeeks'))

