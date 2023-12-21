def trap(heights):

    n=len(heights)
    left=[0]*n
    right=[0]*n

    left_max,right_max=heights[0],heights[n-1]
    i,j=1,n-2

    left[0]=left_max
    right[n-1]=right_max

    while i < n and j > -1:

        left_max=max(left_max,heights[i])
        right_max=max(right_max,heights[j])

        left[i]=left_max
        right[j]=right_max
        i+=1
        j-=1
    
    ans=0

    for i in range(n):
        ans+=min(left[i],right[i])-heights[i]
    return ans


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))


  


