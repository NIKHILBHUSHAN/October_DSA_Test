n=int(input())
arr=[]
parts=input().split()
for x in parts:
    arr.append(int(x))
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
result=""
for i in range(n):
    if i>0:
        result+=" "
    result+=str(arr[i])
print(result)


n=int(input())
arr=[]
parts=input().split()
for x in parts:
    arr.append(int(x))
count=[0]*101
for i in range(n):
    count[arr[i]]+=1
result=""
first=True
for i in range(101):
    for j in range(count[i]):
        if not first:
            result+=" "
        result+=str(i)
        first=False
print(result)