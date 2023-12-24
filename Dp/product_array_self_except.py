#product array self except

def product(nums):
    n=len(nums)

    if not nums:
        return []
    
    ans=[1]*n
    
    for i  in range(n):
        for j in range(n):
            if i==j:
                continue
            else:
               if nums[i]==0:
                   ans[i]=0
               else:
                   ans[i]*=nums[j]
    return ans
    

# print(product([-1,1,2,3,-2]))
        
#using  left ,right

def product_left_right(nums):
    n=len(nums)
    left=[1]*n
    right=[1]*n


    for i in range(1,n):
        left[i]=left[i-1]*nums[i-1]
        right[n-i-1]=right[n-i]*nums[n-i]
    
    for i in range(n):
        nums[i]=left[i]*right[i]
    return nums

#print(product_left_right([0,1,0]))

#short solution for maximum subarray product except shelf
def max_product_subarray(arr):
    B = arr[::-1]
    for i in range(1, len(arr)):
        arr[i] *= arr[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(arr+B)


# next approach for that

def max_product_subarray_another(nums):
    n=len(nums)

    res=-9999
    left=[1]*n
    right=[1]*n


    for i in range(1,n):
        left[i]=left[i-1]*nums[i-1]
        right[n-i-1]=right[n-i]*nums[n-i]
    
        res=max(max(left[i],right[i]),res)
    print(left,right)
    return res


print(max_product_subarray_another([2,3,-2,4]))


        



    

