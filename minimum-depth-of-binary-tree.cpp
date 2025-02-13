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
    int minDepth(TreeNode* root) {
        queue<TreeNode*> q;
        if(root==NULL){
            return 0;
        }
        TreeNode* temp=root;
        q.push(temp);
        int i=0;
        int count=1;
        while(!q.empty()){
            int count1=count;
            count=0;
            i++;
            while(count1!=0){
                TreeNode* temp1=q.front();
                q.pop();
                count1--;
                if( temp1->left==NULL && temp1->right==NULL){
                    return i;
                }
                if( temp1->left){
                    q.push(temp1->left);  
                    count++;
                }
                if( temp1->right){
                    q.push(temp1->right);
                    count++;
                }
            }
        }
        return i;
    }
};