class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1
        while(l < r):
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        piv = l

        if target >= nums[piv] and target <= nums[-1]:
            left , rig = piv , len(nums) - 1
        else:
            left , rig = 0, piv - 1        

        while(left <= rig):
            mid = left + (rig - left)// 2

            if (nums[mid] == target):
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                rig =  mid - 1 
        return -1


          
