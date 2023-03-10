listint=[]
n=int(input("enter no of integers :"))
print("enter integers :")
for i in range(n):
    listint.append(int(input()))
listint.sort()
print("list:",listint)
length = int(n/2)
print(length)
if(n/length!=length):
    median=listint[length]
else:
    median=(listint[length-1]+listint[length])/2
print("median:",median)    
    
