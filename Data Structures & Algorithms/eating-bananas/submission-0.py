class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatime(items: List[int],k : int) -> int:
            time = 0
            for item in items:
                if k > 0:
                    time+= - (- item//k) #ceil division
            return time

        l , r = 1, max(piles)
        minT = float('inf') 

        while( l <= r):
            m = (l + r) // 2
            e = eatime(piles,m)
            if e <= h: 
                minT = m
                r = m - 1
            else:
                l = m + 1 
        return int(minT)

        