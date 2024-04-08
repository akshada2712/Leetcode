class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         heapq.heapify(nums1)
        
#         for i in nums2:
#             heapq.heappush(nums1, i)
#         n = len(nums1)   
#         if n % 2 != 0:
#             m = n // 2 
#             print(nums1[m])
#             l = 0
#             while l != m:
#                 val = heapq.heappop(nums1)
#                 l += 1
#             print(val)
        
        A, B = nums1, nums2
        tot = len(A) + len(B)
        
        if len(B) < len(A):
            A,B = B, A
               
        half = tot // 2 
        l, r = 0, len(A) - 1
        while True:  # run bs on A
            i = (l + r) // 2 
            
            j = half - i  - 2 # since its index of midpoint
            
            aleft = A[i] if i >= 0 else -math.inf
            aright = A[i+1] if (i+1) < len(A)  else math.inf 
            bleft = B[j] if j >= 0 else -math.inf 
            
            bright = B[j+1] if (j + 1) < len(B) else math.inf 
            
            if aleft <= bright and bleft <= aright:
                if tot % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2 
            elif aleft > bright:  # two many elements in A reduce size of A elements
                r = i - 1 
            else:
                l  = i + 1 # increasing left side
                
        
        
        
#         # do binary search on smaller array 
        
#         if len(B) < len(A):
#             A, B = B, A
            
#         l, r = 0 , len(A) - 1
        
        
            
# #         for i in nums2:
# #             nums1.append(i)
            
# #         nums1.sort()
        
        
# #         for 