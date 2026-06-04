class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        dictionary = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            dictionary[key] = dictionary.get(key, []) + [strs[i]]

        return list(dictionary.values())
 
