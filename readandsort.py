n=int(input("enter the no of names:"))
names=[]
print("enter {} names".format(n))
for i in range(n):
    nam=input()
    names.append(nam)
names.sort()
print("the sorted is \n")
for i in names:
    print(i)    