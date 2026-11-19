arr=[10,20,30,40,50]
p=2
x=99
def insert(arr,p,x):
    n=len(arr)
    for i in range(n-1,p-1,-1):
        arr[i]=arr[i-1]#shifting to right as we want to insert node sihft to right without changing
        if i==p:#checking if index=pos 
            arr[i]=x
            break#if found insert and break so previous elements will be as it 
    return arr
result=insert(arr,p,x)
print("array after inserting the element",result)
