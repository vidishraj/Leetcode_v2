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
    ListNode* middleNode(ListNode* head) {
        int count=0;
        ListNode* temp=head;
        while(temp!=NULL){
            count++;
            temp=temp->next;
        }
        if( count==1){
            return head;
        }
        if( count%2==0){
            count=count/2+1;
        }
        else if(count%2!=0){
            count=count/2+1;
        }
        int check=0;
        temp=head;
        while(check!=count){
            check++;
            if( check==count){
                return temp;
            }
            temp=temp->next;
            
        }
        return temp;
    }
};