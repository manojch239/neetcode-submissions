class Solution:
    def trap(self, height: List[int]) -> int:
        Area = 0
        n = len(height)
        l , r = 0 , n - 1

        premax = [0] * n
        sufmax = [0] * n

        premax[0] = height[0]
        for i in range(1,n):
            premax[i] = max(premax[i-1],height[i])
        sufmax[n-1] = height[n-1]
        for j in range(n-2,-1,-1):
            sufmax[j] = max(sufmax[j+1],height[j])

        for i in range(n):
            Area = Area + min(premax[i],sufmax[i]) - height[i]
        return Area


        