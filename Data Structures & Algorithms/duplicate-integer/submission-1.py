class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = nums.sort()
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                continue
            else:
                return True
        return False
        
