class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicate = set(nums)
        if(len(no_duplicate) != len(nums)):
            return True
        return False
        