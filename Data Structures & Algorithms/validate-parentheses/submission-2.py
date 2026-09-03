class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        for current in s:
            if current == "(" or current == "{" or current == "[":
                stack.append(current)
            else:
                if not stack:
                    return False
                matching = stack[-1]

                if current ==")":
                    if matching == "(":
                        stack.pop()
                    else:
                        return False
                elif current == "}":
                    if matching == "{":
                        stack.pop()
                    else:
                        return False
                
                elif current == "]":
                    if matching == "[":
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True



