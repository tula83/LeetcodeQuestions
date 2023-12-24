#count number of subarray  with given k sum

def count_subarray_with_given_sum(arr,k):

    dict_sum={}
    curr_sum=0
    max_length=0
    count=0


    for i,item in enumerate(arr):

        curr_sum+=item

        if curr_sum == k:
           
            max_length = i + 1
        
        
        if curr_sum-k in dict_sum:
            max_length=max(max_length,i-dict_sum[curr_sum-k])
            count+=1



        if curr_sum not in dict_sum:
            dict_sum[curr_sum]=i
        print(max_length)

        
    return count


print(count_subarray_with_given_sum([10, 5, 2, 7, 1, 9],15))
