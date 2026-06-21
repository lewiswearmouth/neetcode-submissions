class Solution:
    # O(n) time O(n) space
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','*','-','/']
        
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == operators[0]:
                    stack.append(int(a) + int(b))
                elif token == operators[1]:
                    stack.append(int(a) * int(b))
                elif token == operators[2]:
                    stack.append(int(a) - int(b))
                else:   
                    stack.append(int(a) / int(b))
        return int(stack[0])
