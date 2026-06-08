class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            product *= nums[i-1]
            prefix[i] = product
        
        suffix = [1 for _ in range(len(nums))]
        product = 1
        for j in range(len(nums)-2, -1, -1):
            product *= nums[j+1]
            suffix[j] = product
        
        output = [_ for _ in range(len(nums))]
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        
        return output
