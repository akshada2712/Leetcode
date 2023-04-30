class MinStack:

    def __init__(self):
        self.nums = []
        

    def push(self, val: int) -> None:
        self.nums.append(val)
        

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]
        

    def getMin(self) -> int:
        return min(self.nums)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()