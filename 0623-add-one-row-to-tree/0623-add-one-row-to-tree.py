# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q = deque()
        q.append((root, 1))
        
        if depth == 1:                      # base case 
            newRoot = TreeNode(val)
            newRoot.left = root 
            return newRoot
        
        # using bfs approach 
        # we would be ttracking the levels
        # at depth - 1 == level: we have found our curr node 
        # create nodes, store curr into temp variable 
        # assign curr.left and curr.right with the new nodes 
        # later assign respective left and right subtress to new nodes formed
        # at any point if level >= height wr can break out the loop
        # add node if the level condiiton isn ot satisfies
        
        
        while q:
            curr, level = q.popleft()
            #print(curr)
            if level == depth - 1:
                temp = TreeNode(curr.val, curr.left, curr.right)
                newLeft = TreeNode(val)
                newRight = TreeNode(val)
                
                curr.left = newLeft 
                curr.right = newRight
                
                newLeft.left = temp.left 
                newRight.right = temp.right 
            elif level >= depth:
                break 
            else:
                if curr.left:
                    q.append([curr.left, level + 1])
                if curr.right:
                    q.append([curr.right, level + 1]) 
                    
                    
        return root