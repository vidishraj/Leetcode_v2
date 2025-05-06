/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* temp=head;
        if( head==NULL){
            return NULL;
        }
        unordered_map<Node*, Node*> gmap;
        while( temp!=NULL){
            Node* newnode= new Node(temp->val);
            gmap[temp]=newnode;
            temp=temp->next;
        }
        temp=head;
        Node* temp1;
        Node* head2=NULL;
        while( temp!=NULL){
            if(head2==NULL){
                temp1=gmap[temp];
                temp1->next=gmap[temp->next];
                temp1->random=gmap[temp->random];
                head2=temp1;
            }
            else{
             temp1=gmap[temp];
             temp1->next=gmap[temp->next];
             temp1->random=gmap[temp->random];   
            }
            temp=temp->next;
        }
        return head2;
    }
};