class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        l = 0
        r = n
        
        while l <= r:
            m = l + (r-l) // 2
            
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m -1
                
        print(l,r)
        
#         pivot = 0
#         while l <= r:
#             m = (r - l) // 2
#             #print(l,r,m)
#             if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
#                 pivot = m
#                 break
                
#             else:
#                 l += 1
#                 r -= 1
#         print(pivot)      

        def binary_search(left, right, target):
            while left <= right:
                mid = left + (right - left) // 2 
                
                if nums[mid] == target:
                    return mid 
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1 
        
        if (ans := binary_search(0, l-1, target)) != -1:
            return ans
        return binary_search(l, n -1, target)
        
        
                 
         
        
#       # modified binary search





    
#         n = len(nums) - 1
#         l, r = 0, n - 1
        
#         while l <= r:
#             m = l + ( r - l) // 2
            
#             # find target
#             if nums[m] == target:
#                 return m
            
#             # subarray on mid's left os sorted 
            
#             elif nums[m] >= nums[l]:
#                 if target >= nums[l] and target < nums[m]:
#                     r = m - 1
#                 else:
#                     l = m + 1
             
#             # subarray is to right
#             else:
#                 if target <= nums[r] and target > nums[m]:
#                     l = m + 1
#                 else:
#                     r = m - 1
                    
#         return -1
                
        
#         if len(nums) == 1:
#             if target == nums[0]:
#                 return 0 
#             else:
#                 return -1
            
#         if len(nums) == 2:
#             if nums[0] == target:
#                 return 0
#             elif nums[1] == target:
#                 return 1
#             else:
#                 return -1
            
            
#         ## find pivot 
#         l = 0
#         r = len(nums)
#         pivot = 0
#         while l <= r:
#             m = (r - l) // 2
#             #print(l,r,m)
#             if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
#                 pivot = m 
#                 break
                
#             else:
#                 l += 1
#                 r -= 1
                
#         # we have got pivot which means the elements towards left of pivot are greater and right are smaller 
#         # print(target)
#         # print(pivot, nums[pivot+1], nums[len(nums)-1] )
#         # print(pivot, nums[pivot], nums[0] )
#         if nums[pivot] == target:
#             return pivot
#         if nums[pivot+1] <= target and nums[len(nums)-1] > target:   # right partition
#             l = pivot + 1
#             r = len(nums) - 1 
            
#             while l <= r:
#                 m = ( r + l) // 2
#                 #print("/",l,m,r)
#                 if nums[m] == target:
#                     return m
#                 elif nums[m] > target:
#                     r = m - 1
#                 else:
#                     l = m + 1
                    
#         if nums[pivot-1] >= target and nums[0] < target:
#             l = 0 
#             r = pivot - 1
            
#             while l <= r:
#                 m = ( r- l) // 2
#                 if nums[m] == target:
#                     return m
#                 elif nums[m] > target:
#                     r = m - 1
#                 else:
#                     l = m + 1 
#         return -1
            
                
                
       