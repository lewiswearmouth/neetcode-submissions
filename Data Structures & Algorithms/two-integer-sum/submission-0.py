class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # O(1) time O(n) space
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in lookup:
                return[lookup[comp], i]

            lookup[nums[i]] = i