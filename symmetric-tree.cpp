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
    bool helper( TreeNode* temp1, TreeNode* temp2){
        if( temp1==NULL && temp2==NULL){
            return true;
        }
        if( temp1==NULL || temp2==NULL){
            return false;
        }
        if(temp1->val==temp2->val){
            return helper(temp1->left, temp2->right)&& helper(temp1->right, temp2->left);
        }
        return false;
    }
    bool isSymmetric(TreeNode* root) {
        if( root->left==NULL && root->right==NULL){
            return true;
        }
        if(root->left==NULL || root->right==NULL){
            return false;
        }
        return helper(root->left, root->right);
    }
};