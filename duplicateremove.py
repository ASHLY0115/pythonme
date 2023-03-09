numlist=[]
print("how many numbers?")
n=int(input())
for i in range(n):
    num=int(input())
    numlist.append(num)

newlist=[]
for i  in numlist:   
    if i not in newlist:
        newlist.append[i] 
print(newlist)        
