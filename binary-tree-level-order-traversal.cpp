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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<int> temp;
        vector<vector<int>> res;
        if( root==NULL){
            return res;
        }
        temp.push_back(root->val);
        res.push_back(temp);
        temp.clear();
        queue<TreeNode*> q;
        int count=0;
        if(root->left){
            q.push(root->left);
            count++;
        }
        if(root->right){
            q.push(root->right);
            count++;
        }
        int count1=0;
        while(!q.empty()){
            count1=count;
            count=0;
            while(count1>0){
                TreeNode* temp1;
                temp1=q.front();
                q.pop();
                count1--;
                temp.push_back(temp1->val);
                if(temp1->left){
                    q.push(temp1->left);
                    count++;
                }
                if(temp1->right){
                    q.push(temp1->right);
                    count++;
                }
            }
            res.push_back(temp);
            temp.clear();
        }
        return res;
    }
};