class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        
        l, h = 1, 10 ** 10
        res = 10 ** 10
        
        def check(d1, d2, cnt1, cnt2, mid):
            notd1 = mid - mid // d1
            notd2 = mid - mid // d2 
            notboth = mid - mid // lcm(d1, d2)
            
            if notd1 >= cnt1 and notd2 >= cnt2 and notboth >= cnt1 + cnt2:
                return True
            else:
                return False
            
        while l <= h:
            mid = l + (h - l) // 2
            if check(divisor1, divisor2, uniqueCnt1, uniqueCnt2, mid):
                res = min(res, mid)
                h = mid - 1
            else:
                l = mid + 1
                
        return res
        
        
#         def check(x):
#             return x - x // divisor1 >= uniqueCnt1 and x - x // divisor2 >= uniqueCnt2 and x - x // math.lcm(divisor1, divisor2) >= uniqueCnt1 + uniqueCnt2

        
#         l = 1 
#         r = 10 ** 10
        
#         while l <= r:
#             m = l + r // 2
            
#             if check(m):
#                 r = m - 1
#             else:
#                 l = m + 1
                
#         return l
            