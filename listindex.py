n=int(input("enter the limit :"))
lista=[]
print("enter the elements")
for i in  range(n) :
    lista.append(input())
    
target = input("enter the target elements :")    
if target in lista:
    print("index of",target,":",lista.index(target))
else:
     print(-1)
    