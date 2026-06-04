# O(nlogn) time O(n) space
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                continue
            else:
                return True
        return False
        
