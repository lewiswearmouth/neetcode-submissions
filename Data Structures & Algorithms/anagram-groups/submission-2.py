class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting O(n * klogk) time, O(n * k) space
        dictionary = defaultdict(list)
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            dictionary[key].append(strs[i])

        return list(dictionary.values())
 
