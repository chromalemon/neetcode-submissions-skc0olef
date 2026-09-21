# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr.right:
            curr = curr.right
        parent = [None] * (curr.val + 1)

        queue = deque()
        queue.append(root)
        while queue:
            curr = queue.popleft()
            if curr.left:
                parent[curr.left.val] = curr
                queue.append(curr.left)
            if curr.right:
                parent[curr.right.val] = curr
                queue.append(curr.right)
        
        branch = set()
        curr = p
        while curr is not None:
            branch.add(curr.val)
            curr = parent[curr.val]
        curr = q
        while curr is not None:
            if curr.val in branch:
                return curr
            curr = parent[curr.val]