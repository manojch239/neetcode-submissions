class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #dic 
        # num_dic = {}
        # for num in nums:
        #     if num in num_dic:
        #         return True
        #     else:
        #         num_dic[num] = 1
        #         return False
        return len(nums) != len(set(nums))
        