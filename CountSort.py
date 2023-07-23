def countSort(arr):

    maxi=max(arr)
    count=[0]*(maxi+1)

    for i in arr:
        count[i]+=1

    result=[]
    for i in range(len(count)):
        result.extend(count[i]*[i])
    return result

arr=list(map(int,input().split()))
print(countSort(arr))
