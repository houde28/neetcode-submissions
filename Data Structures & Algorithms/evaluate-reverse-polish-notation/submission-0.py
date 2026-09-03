class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                val1= int(stack.pop())
                val2 = int(stack.pop())
                if token == "+":
                    stack.append(val1+val2)
                elif token == "-":
                    stack.append(val2-val1)
                elif token == "*":
                    stack.append(val2*val1)
                else:
                    stack.append(val2/val1)
            else:
                stack.append(token)
        
        result = int(stack[-1])
        return result
        