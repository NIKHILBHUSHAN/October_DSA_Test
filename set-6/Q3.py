parts=input().split()
m=int(parts[0])
n=int(parts[1])
A=[]
B=[]
parts=input().split()
for x in parts:
    A.append(int(x))
parts=input().split()
for x in parts:
    B.append(int(x))
arr=[]
for i in range(m):
    arr.append(A[i])
for i in range(n):
    arr.append(B[i])
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
result=[]
for i in range(len(arr)):
    if i==0 or arr[i]!=arr[i-1]:
        result.append(arr[i])
output=""
for i in range(len(result)):
    if i>0:
        output+=" "
    output+=str(result[i])
print(output)


parts=input().split()
m=int(parts[0])
n=int(parts[1])
A=[]
B=[]
parts=input().split()
for x in parts:
    A.append(int(x))
parts=input().split()
for x in parts:
    B.append(int(x))
i=0
j=0
result=[]
while i<m and j<n:
    if A[i]<B[j]:
        x=A[i]
        i+=1
    elif A[i]>B[j]:
        x=B[j]
        j+=1
    else:
        x=A[i]
        i+=1
        j+=1
    if len(result)==0 or result[len(result)-1]!=x:
        result.append(x)
while i<m:
    if len(result)==0 or result[len(result)-1]!=A[i]:
        result.append(A[i])
    i+=1
while j<n:
    if len(result)==0 or result[len(result)-1]!=B[j]:
        result.append(B[j])
    j+=1
output=""
for i in range(len(result)):
    if i>0:
        output+=" "
    output+=str(result[i])
print(output)