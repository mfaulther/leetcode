#https://leetcode.com/problems/binary-tree-level-order-traversal
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            curr_list = []
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr_list)
        return res