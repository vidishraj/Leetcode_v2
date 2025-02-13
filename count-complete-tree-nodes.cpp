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
    int countNodes(TreeNode* root) {
        if( root==NULL){
            return 0;
        }
        if( root->left==NULL){
            return 1;
        }
        TreeNode* temp1=root;
        while(temp1->left!=NULL){
            temp1=temp1->left;
        }
        int count=1;
        vector<TreeNode*> temp;
        temp.push_back(root);
        TreeNode* temp2=NULL;
        while(temp.front()->left!=temp1){
            temp2=temp.front();
            temp.push_back(temp2->left);
            count++;
            temp.push_back(temp2->right);
            count++;
            temp.erase(temp.begin());
        }
        //now just empty the queue
        while(!temp.empty()){
            if( temp.front()->left){
                count++;
            }
            if( temp.front()->right){
                count++;
            }
            temp.erase(temp.begin());
        }
        return count;
    }
};