class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        new_s = s.lower()

        while left < right:
            if(not new_s[left].isalnum()):
                left+=1
            elif(not new_s[right].isalnum()):
                right-=1
            elif(new_s[left] == new_s[right]):
                left+=1
                right-=1
            else:
                return False
        return True
