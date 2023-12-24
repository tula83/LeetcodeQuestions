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

print(product_less_than_k([10,5,2,6],100))

