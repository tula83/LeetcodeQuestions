def findMaxlength(arr):
    n=len(arr)
    result,count=0,0

    lookup={0:-1}

    for i,num in enumerate(arr):
        
        count+=1 if num==1 else -1

        

        if count in lookup:
            result=max(result,i-lookup[count])

        else:
            lookup[count]=i
        print(lookup,count)

    return result




print(findMaxlength([1,0,1]))