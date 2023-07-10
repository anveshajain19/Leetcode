class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        leftDepth = sys.maxsize
        rightDepth = sys.maxsize
        if root.left is not None:
            leftDepth = self.minDepth(root.left)
        if root.right is not None:
            rightDepth = self.minDepth(root.right)
        return 1 + min(leftDepth, rightDepth)
