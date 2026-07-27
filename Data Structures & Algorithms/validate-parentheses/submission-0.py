class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            element = stack[-1]
            if (element == "{" and i == "}") or (element == "[" and i == "]") or (element == "(" and i == ")"):
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
            
        