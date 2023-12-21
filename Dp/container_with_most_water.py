def max_area(heights):

    n=len(heights)
    left,right=0,n-1
    ans=-9999


    while left < right:
        ans=max( min(heights[left],heights[right])* (right-left) , ans )
       
        left,right=(left+1,right) if heights[left] < heights[right] else (left,right-1)
      
    return ans

print(max_area([1,8,6,2,5,4,8,3,7]))