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

#print(Subarray_sum_equals_k([1,1,1],2))


# maximum subarray sum
def maxSubArray(nums):
        curr_sum,till=0,nums[0]

        for item in nums:
            curr_sum+=item
            till=max(till,curr_sum)
            
            if curr_sum < 0:
                curr_sum=0
        return  till

#print(maxSubArray([-1,1,-3,4]))

# good subarray
# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a subarray where:
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.




# intervals between identical elements
import collections
def getDistances(arr):
    n=len(arr)
    lookup=collections.defaultdict(list)

    for i , x in enumerate(arr):
        lookup[x].append(i)

    print(lookup)
    
    result=[0]*n

    for idxs in lookup.values():
        prefix=[0]

        for i in idxs:
            prefix.append(prefix[-1]+i)

        print(prefix)

        for i,idx in enumerate(idxs):
            result[idx]=(idx*(i+1)-prefix[i+1])+ ( (prefix[len(idxs)]-prefix[i])-idx*(len(idxs)-i) )

           

            
        
    return result


print(getDistances([2,1,3,1,2,3,3]))