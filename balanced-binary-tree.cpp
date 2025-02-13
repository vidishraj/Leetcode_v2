/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool flag;
    int count( TreeNode* root){
        if(root==NULL){
            return 0;
        }
        int l=1+count(root->left);
        int r=1+count(root->right);
        if(abs(l-r)>1){
            flag=false;
        }
        return max(l,r);
    }
    bool isBalanced(TreeNode* root) {
        flag=true;
        count(root);
        return flag;
    }
};