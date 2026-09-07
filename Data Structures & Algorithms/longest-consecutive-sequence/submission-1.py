class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the elements 
        # remove duplicates 
        # res = 0
        # store = set(nums)
        
        # for num in nums:
        #     streak , curr = 0 , num
        #     while curr in store:
        #         streak += 1
        #         curr += 1 
        #     res = max(res,streak)
        # return res

        numSet = set(nums)
        l  = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1 
                l = max(length, l)
        return l
        