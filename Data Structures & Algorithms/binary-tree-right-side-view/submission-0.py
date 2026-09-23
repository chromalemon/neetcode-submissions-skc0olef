# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque()
        queue.append((root, 0))
        seen = set()
        res = []

        while queue:
            node, depth = queue.popleft()
            if depth not in seen:
                res.append(node.val)
                seen.add(depth)
            if node.right:
                queue.append((node.right, depth+1))
            if node.left:
                queue.append((node.left, depth+1))

        return res