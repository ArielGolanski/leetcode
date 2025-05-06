class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        result = 0

        def dfs(root):
            nonlocal result
        
            if not root:
                return 0
        
            left = dfs(root.left)
            right = dfs(root.right)
            result = max(result, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return result
        