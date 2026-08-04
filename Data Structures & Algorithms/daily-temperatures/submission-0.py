class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            stack.append([temperatures[i], 0, False])
            j = 0
            while j < i:
                if stack[j][0] < temperatures[i] and not stack[j][2]:
                    stack[j][1] = i - j
                    stack[j][2] = True
                j += 1
        res = []
        for i in stack:
            res.append(i[1])
        return res