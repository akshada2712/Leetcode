class MedianFinder:

    def __init__(self):
        self.res = []
        

    def addNum(self, num: int) -> None:
        self.res.append(num)
        

    def findMedian(self) -> float:
        n = len(self.res)
        self.res.sort()
        mid = n // 2
        if n % 2 != 0:
            return self.res[mid]
        else:
            return (self.res[mid] + self.res[mid - 1]) / 2
        
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()