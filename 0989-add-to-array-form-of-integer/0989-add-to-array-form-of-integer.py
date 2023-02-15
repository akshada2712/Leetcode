class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        number = ''.join(str(x) for x in num)
        number = int(number)
        sum_ = number + k
        return [int(i) for i in str(sum_)]
        