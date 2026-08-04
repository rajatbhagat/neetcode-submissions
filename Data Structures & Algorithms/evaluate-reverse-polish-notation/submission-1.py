class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        symbol_set = set(['*', '+', '/', '-'])
        for i in tokens:
            if i not in symbol_set:
                stack.append(int(i))
            else:
                print(stack)
                res = 0
                one = stack.pop()
                two = stack.pop()
                if i == '*':
                    res = one * two
                elif i == '+':
                    res = one + two
                elif i == '-':
                    res = two - one
                elif i == '/':
                    res = int(two / one)
                stack.append(res)
        return stack[-1]