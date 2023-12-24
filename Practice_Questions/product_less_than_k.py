def product_less_than_k(nums,k):

    n,res,start,prod=len(nums),0,0,1


    for i in range(n):

        if nums[i] >=k:
            start=i+1
            prod=1

        else:
            prod*=nums[i]

            while prod>=k:
                prod/=nums[start]
                start+=1
            
            res+=i-start+1
    return res

#print(product_less_than_k([10,5,2,6],100))


# related question  Subarray Sum Equals K
#using  dictionary sum

def Subarray_sum_equals_k(nums,k):

    #n=len(nums)
    dict_sum={0:1}
    sum=0
    count=0

    for item in nums:

        sum+=item

        count+=dict_sum.get(sum-k,0)

        dict_sum[sum]=dict_sum.get(sum,0)+1
    
    return count

print(Subarray_sum_equals_k([1,1,1],2))




