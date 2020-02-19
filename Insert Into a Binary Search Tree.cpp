//https://leetcode.com/problems/insert-into-a-binary-search-tree
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* curr = root;
        while (true)
        {
            if (val > curr->val)
            {
                if (curr->right == NULL)
                {
                    curr->right = new TreeNode(val);
                    break;
                }
                curr = curr->right;
            }
            else
            {
                if (curr->left == NULL)
                {
                    curr->left = new TreeNode(val);
                    break;
                }
                curr = curr->left;
            }
        }
        return root;
    }
};