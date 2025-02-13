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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* hold=head;
        ListNode* run=head;
        while(hold!=NULL){
            if( run->next!=NULL && run->next->val==run->val){
                while(run->next!=NULL && run->next->val==run->val){
                    run=run->next;
                }
                hold->next=run->next;
            }
            hold=hold->next;
            run=hold;
        }
        return head;
    }
};