class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        
        lookup_s, lookup_t = {}, {}
        for i in range(len(s)): 
            lookup_s[s[i]] = 1 + lookup_s.get(s[i], 0)
            lookup_t[t[i]] = 1 + lookup_t.get(t[i], 0)

        for i in range(len(s)):
            if lookup_s.get(s[i], 1) != lookup_t.get(s[i], 0):
                return False

        return True