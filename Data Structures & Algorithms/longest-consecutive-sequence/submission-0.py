class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        start_sequence = []
        for num in set_nums:
                if num - 1 not in set_nums:
                        start_sequence.append(num)

        res = 0
        max_res = 0
        for num in start_sequence:
                res = 1
                next_num = num + 1
                while next_num in set_nums:
                        res += 1
                        next_num += 1
                if res > max_res:
                        max_res = res                    
        return max_res