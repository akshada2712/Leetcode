class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n,3)
        return abs(x - round(x)) < 1e-10
        # if x.is_integer():
        #     return True
        # else:
        #     return False
#         if n <= 0:
#             return False
#         x = math.log(n) / math.log(3) 
#         return x % 1 == 0
        