class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        i, j = 0,(len(height)-1)
        while(i<j):
            vol = min(height[i],height[j])*(j-i)
            maxvol = max(maxvol,vol)  
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1         
        return maxvol
        
