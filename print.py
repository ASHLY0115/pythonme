f=open("numbers","w")
num=input("enter the numbers :")
f.write(num)
f.close()
F=open("numbers","r")

"""""
for line in F:
    print(line)
    lines=line.split()
    sum=0
    for ch in lines:
        sum=sum+int(ch)
    print("sum = ",sum)    
    """""