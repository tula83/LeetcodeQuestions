def largestRectangle(heights):
    
    stack=[]
    n=len(heights)
    left_limit=[0]*n
    right_limit=[0]*n

    #for storing left  index
    for  i in range(n):
        if not stack:
            left_limit[i]=0
        else:
            while stack and  heights[stack[-1]]>=heights[i]:
                stack.pop()
            left_limit[i]=stack[-1]+1 if stack else -1
        stack.append(i)
    stack.clear()

    #for right limit
    for i in range(n-1,-1,-1):
        
        if not stack:
            right_limit[n-1]=n-1

        else:
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            right_limit[i]=stack[-1]-1  if stack else n-1
        stack.append(i)
    
    area=-19999
    for i  in range(n):
        area=max(area,(right_limit[i]-left_limit[i]+1)*heights[i])
    
    
    return area


heights=[2,4]

print(f'largest rectange having area is {largestRectangle(heights)}')

        

    



