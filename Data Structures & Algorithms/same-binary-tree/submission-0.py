# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q = deque([p, q])

        while q:
            node1 = q.popleft()
            node2 = q.popleft()

            if not node1 and not node2:
                continue

            if (not node1)^(not node2):
                return False

            if node1.val != node2.val:
                return False
            
            q.append(node1.left)
            q.append(node2.left)
            q.append(node1.right)
            q.append(node2.right)

        return True