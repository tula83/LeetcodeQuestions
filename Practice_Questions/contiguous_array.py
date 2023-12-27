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




#print(findMaxlength([1,0,1]))



def subarraysDivByK(self, nums, k):

        n=len(nums)
        count=0
        
        for i in range(n):
            for  j in range(i,n):
                if i==j:
                    if nums[i]%k==0:
                        count+=1
                else:
                    result=sum(nums[i:j+1])
                   
                    if result%k==0:
                        
                        count+=1
                
                
               
                
                
        
        return count




def subarrayDivByK(arr,k):

    sum_remainder_freq={0:1}
    running_sum=0
    count=0


    for num in arr:
        running_sum=(running_sum+num)%k
        if running_sum < 0:
            running_sum+=k


        if running_sum in sum_remainder_freq:
            count+=sum_remainder_freq.get(running_sum)

        
        sum_remainder_freq[running_sum]=sum_remainder_freq.get(running_sum,0)+1

    return count



#print(subarrayDivByK([4,5,0,-2,-3,1],5))

#You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
#Return the total number of bad pairs in nums.
import collections
def count_bad_pairs(nums):
    n=len(nums)
    result=n*(n-1)//2

    cnt=collections.Counter()
    
    
    for i ,x in enumerate(nums):
        print(f'x - i : {x-i}')
        result-=cnt[x-i]
        cnt[x-i]+=1
        print(f"i: {i}, x: {x}, result: {result}, cnt: {cnt}")
    print(cnt)
    return result


print(count_bad_pairs([4,1,3,3]))


