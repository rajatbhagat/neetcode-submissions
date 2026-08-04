class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        if not self.stack:
            return None
        res = self.stack.pop()
        if res == self.min_val:
            if not self.stack:
                self.min_val = float('inf')
            else:
                self.min_val = min(self.stack)
        return res

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.min_val
