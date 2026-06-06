class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap iterate through array add 1 to each value, key is num
        # sort values after

        # sort array then iterate until k unique numbers
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1

        hash_sort = sorted(freq, key=freq.get, reverse = True)
        
        return hash_sort[:k]