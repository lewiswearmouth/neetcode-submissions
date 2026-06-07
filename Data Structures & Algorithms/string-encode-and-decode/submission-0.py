class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        if len(strs) != 0:
            length = 0
            for each in strs:
                encoded_string += str(len(each)) + "#" + each
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) != 0:
            res_str = ""
            i = 0
            while i < len(s):
                j = i
                while s[j] != "#":
                    j += 1
                length = int(s[i:j])
                i = j + 1
                while length > 0: 
                    res_str += s[i]
                    length -= 1
                    i+=1
                res.append(res_str)
                res_str = ""
        return res
            