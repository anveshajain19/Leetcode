from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = deque()
        q.append(root)
        level = 0
        while q:
            levelsize = len(q)
            current_level = []
            for _ in range(levelsize):
                current = q.popleft()
                current_level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            if level % 2 != 0:
                current_level = current_level[::-1]
            result.append(current_level)
            level += 1
        return result