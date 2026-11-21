n=int(input())
arr=[]
parts=input().split()
for x in parts:
    arr.append(int(x))
freq={}
for i in range(n):
    x=arr[i]
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
for i in range(n):
    best=i
    for j in range(i+1,n):
        a=arr[j]
        b=arr[best]
        if freq[a]<freq[b] or (freq[a]==freq[b] and a>b):
            best=j
    temp=arr[i]
    arr[i]=arr[best]
    arr[best]=temp
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
freq={}
ids=[]
for i in range(n):
    x=arr[i]
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
        ids.append(x)
temp=[0]*len(ids)
def before(a,b):
    if freq[a]<freq[b]:
        return True
    if freq[a]>freq[b]:
        return False
    return a>b
def merge_sort(left,right):
    if left>=right:
        return
    mid=(left+right)//2
    merge_sort(left,mid)
    merge_sort(mid+1,right)
    i=left
    j=mid+1
    k=left
    while i<=mid and j<=right:
        if before(ids[i],ids[j]):
            temp[k]=ids[i]
            i+=1
        else:
            temp[k]=ids[j]
            j+=1
        k+=1
    while i<=mid:
        temp[k]=ids[i]
        i+=1
        k+=1
    while j<=right:
        temp[k]=ids[j]
        j+=1
        k+=1
    for i in range(left,right+1):
        ids[i]=temp[i]
merge_sort(0,len(ids)-1)
output=""
first=True
for i in range(len(ids)):
    x=ids[i]
    for j in range(freq[x]):
        if not first:
            output+=" "
        output+=str(x)
        first=False
print(output)