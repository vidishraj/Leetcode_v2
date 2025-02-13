/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
//we will do level traversal and save it in an array and then point the next accordingly 
class Solution {
public:
    Node* connect(Node* root) {
        queue<Node*> q;
        if(root==NULL){//empty list
            return root;
        }
        else{
            Node* temp=root;
            q.push(temp);
            int count=1;
            int count1=0;
            while(!q.empty()){
                while(count>0){
                    //we have to point the pointers
                    temp=q.front();
                    q.pop();
                    if(count-1==0){
                        temp->next==NULL;
                    }
                    else if(count-1!=0){
                        temp->next=q.front();
                    }
                    if(temp->left){
                        q.push(temp->left);
                        count1++;
                    }
                    if(temp->right){
                        count1++;
                        q.push(temp->right);
                    }
                    count--;
                }
                count=count1;
                count1=0;
            }
            return root;
        }
    }
};