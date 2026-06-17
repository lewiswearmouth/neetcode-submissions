class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []
        for c in s:
            if c in lookup.values():
                stack.append(c)
            else:
                if not stack or stack.pop() != lookup[c]:
                    return False
        return not stack

        