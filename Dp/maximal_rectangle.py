class Solution:

    def largestRectangleArea(self, heights):

        n=len(heights)

        left=[0]*n
        right=[0]*n
        stack=[]

        for i in range(n):
            if not stack:
                left[i]=0
            else:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                left[i]=stack[-1]+1 if stack else 0
            stack.append(i)
        stack.clear()


        for i in range(n-1,-1,-1):
            
            if not stack:
                right[i]=n-1
            else:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                right[i]=stack[-1]-1 if stack else n-1
            stack.append(i)
        
        area=0

        for i  in range(n):
            area=max(area,(right[i]-left[i]+1)*heights[i])
        
        return area


    def maximalRectangle(self, matrix) -> int:

        n=len(matrix)
        m=len(matrix[0])

        max_area=-9999
        heights=[0]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            max_area=max(max_area,self.largestRectangleArea(heights))
        return max_area
       
        