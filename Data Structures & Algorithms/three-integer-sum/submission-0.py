class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        output = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]
            j = i + 1
            k = n - 1
            while ( j < k):
                csum = nums[j] + nums[k]
                if csum > target:
                    k = k - 1
                elif csum < target:
                    j = j + 1 
                else: 
                    output.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    k = k - 1 
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return output
        