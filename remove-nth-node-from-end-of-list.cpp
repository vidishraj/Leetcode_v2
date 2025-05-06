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
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        //Another approach might be to actually count the nodes first
        int count=0;
        ListNode* temp=head;
        while( temp!=NULL){
            temp=temp->next;
            count++;
        }
        temp=head;
        int del=count-n;
        if( del==0){//delete first node
            head=temp->next;
            return head;
        }
        else{
            ListNode* temp1=head;
            count=0;
            while(count!=del){
                count++;
                temp1=temp;
                temp=temp->next;
            }
            temp1->next=temp->next;
            
        }
        return head;
    }
};