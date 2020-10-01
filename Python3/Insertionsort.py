def insertionSort(arr, n) :  
    #Your code goes here
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break
print('Number of Elements in Array ')
n = int(input())
l=[]
for i in range(n):
    print('Enter the element no.' +str(i))
    l.append(int(input()))
insertionSort(l,n)
print('Elements in Sorted Array ')
for i in l:
    print(i,end=' ')