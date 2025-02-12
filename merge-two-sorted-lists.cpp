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
ListNode* addtoList(ListNode* newnode, int val){
    if(newnode->val==-200){
        newnode->val=val;
    }
    else{
        newnode->next=new ListNode(val);
        newnode=newnode->next;
    }
    return newnode;
}
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==NULL and list2==NULL){
            return NULL;
        }
        ListNode* newnode=new ListNode(-200);
        ListNode* res=newnode;
        while(list1!=NULL or list2!=NULL){
            if( list1 and list2 and list1->val < list2->val){
                newnode=addtoList(newnode, list1->val);
                list1=list1->next;
            }
            else if(list1 and list2 and list1->val > list2->val){
                newnode=addtoList(newnode, list2->val);
                list2=list2->next;
            }
            else if(list1 and list2 and list1->val == list2->val){
                newnode=addtoList(newnode, list1->val);
                list1=list1->next;
                newnode=addtoList(newnode, list2->val);
                list2=list2->next;
            }
            else if(list1==NULL){
                newnode=addtoList(newnode, list2->val);
                list2=list2->next;
            }
            else if(list2==NULL){
                newnode=addtoList(newnode, list1->val);
                list1=list1->next;
            }
        }
        return res;
    }
};