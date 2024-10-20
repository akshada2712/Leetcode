class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        
        # we can compute prefix and postfix arrays 
        # then result[i] = prefix[i-1] * postfix[i+1]
        # O(n) space can be done in O(1) : using two pointers
        # initialize pre and post = 1 
        
        
        pre = 1 
        post = 1
        
        # assign every valu to output as pre , then calculate prefix_num
        for i in range(len(nums)):
            res[i] = pre 
            pre *= nums[i]
            
        # assign evry value to post but multiplying with the present (pre) value, then calculate post
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
            
        # return output
        return res