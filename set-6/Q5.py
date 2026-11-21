n=int(input())
arr=[]
parts=input().split()
for x in parts:
    arr.append(int(x))
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
output=""
for i in range(n):
    if i>0:
        output+=" "
    output+=str(arr[i])
print(output)


n=int(input())
arr=[]
parts=input().split()
for x in parts:
    arr.append(int(x))
stack=[]
stack.append((0,n-1))
while len(stack)>0:
    current=stack.pop()
    low=current[0]
    high=current[1]
    if low>=high:
        continue
    pivot=arr[(low+high)//2]
    lt=low
    mid=low
    gt=high
    while mid<=gt:
        if arr[mid]<pivot:
            temp=arr[lt]
            arr[lt]=arr[mid]
            arr[mid]=temp
            lt+=1
            mid+=1
        elif arr[mid]>pivot:
            temp=arr[mid]
            arr[mid]=arr[gt]
            arr[gt]=temp
            gt-=1
        else:
            mid+=1
    if lt-low<high-gt:
        if gt+1<high:
            stack.append((gt+1,high))
        if low<lt-1:
            stack.append((low,lt-1))
    else:
        if low<lt-1:
            stack.append((low,lt-1))
        if gt+1<high:
            stack.append((gt+1,high))
output=""
for i in range(n):
    if i>0:
        output+=" "
    output+=str(arr[i])
print(output)