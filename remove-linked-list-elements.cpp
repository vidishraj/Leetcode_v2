/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
static const auto fast=[](){ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);return nullptr;}();
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* temp=head;
        ListNode* runner=NULL;
        while( temp!=NULL){
            if( temp->val==val){
                if(runner==NULL){
                    head=temp->next;
                    temp=head; 
                }
                else{
                    if( temp->next){
                        runner->next=temp->next;
                        temp=temp->next;
                    }
                    else{
                        runner->next=NULL;
                        temp=NULL;
                    }
                }
            }
            else{
                runner=temp;
                temp=temp->next;
            }
        }
        return head;
    }
};