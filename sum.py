sum=0
f=open("integers.txt","w")
print("enter 10 numbers")
for i in range(10):
    num=input()
    f.write(num+"\n")
f.close()   
f=open("integers.txt","r")
while True:
    line=f.readline()
    if line=="" :
        break
    else:
        n=int(line)
        sum=sum+n
print(sum)