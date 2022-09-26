#Concatenate two numbers
#Brute force Approach

def subset(arr,x):
    d={}
    c=0
    for i in range(len(arr)):
        for j in range(i+1):
            d[str(i)+str(j)]=int(str(arr[i])+str(arr[j]))
    
    for i in d.values():
        if x==i:
            c=c+1
    print(c)
n=int(input("Size: "))
X=int(input("Enter the X: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
ans=subset(a,X)
