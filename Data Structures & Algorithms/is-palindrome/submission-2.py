class Solution:
    # O(n) time, O(1) space
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if(not self.alphaNum(s[left])):
                left+=1
            elif(not self.alphaNum(s[right])):
                right-=1
            elif(s[left].lower() == s[right].lower()):
                left+=1
                right-=1
            else:
                return False
        return True

    def alphaNum(self,c):
       return ((ord(c) >= ord('A') and ord(c) <= ord('Z')) 
           or (ord(c) >= ord('a') and ord(c) <= ord('z')) 
           or (ord(c) >= ord('0') and ord(c) <= ord('9')) )