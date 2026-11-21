'''
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
'''

n=int(input())
arr=[]
parts=input().split()
for x in parts:
    arr.append(int(x))
low=0
mid=0
high=n-1
while mid<=high:
    if arr[mid]==0:
        temp=arr[low]
        arr[low]=arr[mid]
        arr[mid]=temp
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:
        temp=arr[mid]
        arr[mid]=arr[high]
        arr[high]=temp
        high-=1
result=""
for i in range(n):
    if i>0:
        result+=" "
    result+=str(arr[i])
print(result)