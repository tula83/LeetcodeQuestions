import heapq

def kth_largest(nums,k):
    heap=nums[:k]

    heapq.heapify(heap)
   

    for num in nums[k:]:

        if num > heap[0]:
            heapq.heappop(heap)
            
            heapq.heappush(heap,num)

            print(heap)

    return heap[0]

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k_value = 4


#print(kth_largest(numbers,k_value))

