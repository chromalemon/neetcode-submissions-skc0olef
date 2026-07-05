# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.maximum = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.maximum = max(self.maximum, left+right)
            return max(left, right) + 1
        
        dfs(root)
        return self.maximum