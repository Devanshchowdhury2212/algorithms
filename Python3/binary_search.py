print('Number of Elements in Sorted Array ')
n = int(input())
l=[]
for i in range(n):
    print('Enter the element no.' +str(i))
    l.append(int(input()))
print('Element to be Searched in Sorted Array ')
f = int(input())
s,e = 0,n
m = (s+e)//2
while s<=m and m<=e:
    # print(s,m,e)
    if s==m:
        if l[s]==f:
            print('Found at postion '+str(s))
            break
        else:
            print('Not Found')
            break 
    elif s==m:
        if l[e]==f:
            print('Found at postion '+str(e))
            break
        else:
            print('Not Found')
            break
    elif l[m]>f:
        e = m
    else:
        s = m
    m = (s+e)//2

