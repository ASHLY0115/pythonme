numbers=[]
def min_max(numbers):
    n=int(input("enter the limit:"))
    for i in range(n):
        l=int(input())
        numbers.append(l)
    min1=min(numbers)
    max1=max(numbers)
    return(min1,max1)
x,y=min_max(numbers)
print(x,y)
