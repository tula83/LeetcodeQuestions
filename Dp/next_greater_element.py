# this contains  variations of questions solved with next_greater element approach
def  next_greater_element(arr):
    s=[]
    n=len(arr)

    for i in range(n):
        while s and s[-1].get("value") < arr[i]:
            d=s.pop()
            arr[d.get("index")]=arr[i]
        s.append({'value':arr[i],'index':i})
    while s:
        d=s.pop()
        arr[d.get("index")]=-1
    return arr

print(next_greater_element([4,1,2]))


# for  finding next greater element of first array in second array


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        n=len(nums1)
        s=[]
        mp={}
        for  i in range(len(nums2)):
            while s and  s[-1].get('value') < nums2[i]:
                d=s.pop()
                mp[d.get("value")]=nums2[i]
                nums2[d.get("index")]=nums2[i]
                
            s.append({'index':i,'value':nums2[i]})
        while s: 
            d=s.pop()
            mp[d.get("value")]=-1
            nums2[d.get('index')]=-1
        print(mp)
        
        for index,value  in enumerate(nums1):
            nums1[index]=mp.get(value,-1)
       
        
        
        return nums1
            

        
# daily temperature
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number 
# of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
    

class Solution:
    def dailyTemperatures(self, arr):
        n=len(arr)
        s=[]

        if not arr:
            return []
        
        for i in range(n):
            while s and s[-1].get('value') < arr[i]:
                d=s.pop()
                index=d.get('index')
                arr[index]=i-index
            s.append({'index':i,'value':arr[i]})

        while s:
            d=s.pop()
            arr[d.get('index')]=0
        return  arr



