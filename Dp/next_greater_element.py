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
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
            

        

