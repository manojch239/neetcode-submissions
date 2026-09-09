class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # nums.sort()
        # output = []
        # n = len(nums)
        
        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     target = -1 * nums[i]
        #     j = i + 1
        #     k = n - 1
        #     while ( j < k):
        #         csum = nums[j] + nums[k]
        #         if csum > target:
        #             k = k - 1
        #         elif csum < target:
        #             j = j + 1 
        #         else: 
        #             output.append([nums[i],nums[j],nums[k]])
        #             j = j + 1
        #             k = k - 1 
        #             while nums[j] == nums[j-1] and j < k:
        #                 j += 1

        # return output


        # Using Two pointers
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l+= 1
                else:
                    res.append([a, nums[l],nums[r]])
                    l+=1 
                    r-=1
                    while nums[l] == nums[l -1] and l < r:
                        l +=1

        return res


        