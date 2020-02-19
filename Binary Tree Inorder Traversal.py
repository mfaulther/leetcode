#https://leetcode.com/problems/binary-tree-inorder-traversal
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
            res = []
            if not root:
                return res
            stack = []
            stack.append(root)
            while stack:
                curr = stack[-1]
                if (curr.left):
                    stack.append(curr.left)
                    curr.left = None
                else:
                    stack.pop()
                    res.append(curr.val)
                    if curr.right:
                        stack.append(curr.right)
            return res