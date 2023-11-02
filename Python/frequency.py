def findFrequency(arr):
    count={}
    n=len(arr)
    for i in range(n):
        if arr[i] in count:
            count[arr[i]]+=1
        else:
            count[arr[i]]=1
    print(count)

findFrequency(['a','b','c'])

