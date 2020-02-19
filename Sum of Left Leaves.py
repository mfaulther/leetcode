#https://leetcode.com/problems/sum-of-left-leaves
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        
        def func(root):
            if root:
                if root.left:
                    if not root.left.left and not root.left.right:
                        self.res += root.left.val
                func(root.left)
                func(root.right)
        
        func(root)
        return self.res 