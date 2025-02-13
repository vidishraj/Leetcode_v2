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
    vector<string> ans;
    string arrow="->";
    void helper(TreeNode* root, string a){
        if(a.empty()){
            string temp=to_string(root->val);
            a=temp;
            if(root->left){
                helper(root->left,a);
            }
            if(root->right){
                helper(root->right,a);
            }
        }
        else if(root->right==NULL && root->left==NULL){//leaf node case
            string temp=to_string(root->val);
            a+=arrow;
            a+=temp;
            ans.push_back(a);
            return;
        }
        else{
            a+=arrow;
            string temp=to_string(root->val);
            a+=temp;
            if(root->left){
                helper(root->left,a);
            }
            if(root->right){
                helper(root->right,a);
            }
        }
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        string a;
        if(root->left==NULL && root->right==NULL){
            a=to_string(root->val);
            ans.push_back(a);
            return ans;
        }
        else{
            helper(root, a);
        }
        return ans;
    }
};