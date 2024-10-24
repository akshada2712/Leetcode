class MedianFinder:

    def __init__(self):
        self.nums = []
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        size = len(self.nums)
        self.nums.sort()
        mid = size // 2 
        if size % 2 != 0:
            return self.nums[mid]
        else:
            return (self.nums[mid - 1] + self.nums[mid]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()