class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        l , r = 0, len(heights) -1

        while( l < r):
            Area = min(heights[l],heights[r]) * (r - l)
            mArea = max(mArea,Area)

            if heights[l] > heights[r]:
                r = r-1
            else:
                l = l+1
        return mArea