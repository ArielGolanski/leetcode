class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False
        else:
            if p.val == q.val:
                return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        
