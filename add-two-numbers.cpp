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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        vector<int> list1;
        vector<int> list2;
        ListNode* temp=l1;
        while(temp!=NULL){
            list1.push_back(temp->val);
            temp=temp->next;
        }
        temp=l2;
        while(temp!=NULL){
            list2.push_back(temp->val);
            temp=temp->next;
        }
        reverse(list1.begin(), list1.end());
        reverse(list2.begin(), list2.end());
        int i=list1.size()-1;
        int j=list2.size()-1;
        vector<int>res;
        int remainder=0;
        while(i>=0 && j>=0){
            int num1=list1[i];
            int num2=list2[j];
            int ans=num1+num2;
            if( remainder==1){
                ans+=1;
                remainder=0;
            }
            if( ans>=10){
                ans%=10;
                remainder=1;
            }
            res.push_back(ans);
            i--;
            j--;
        }
        while(i>=0){
            int ans=list1[i];
            if( remainder==1){
                ans+=1;
                if(ans>=10){
                    ans%=10;
                    remainder=1;
                }
                else{
                    remainder=0;
                }
                res.push_back(ans);
                
            }
            else{
                res.push_back(ans);
            }
            i--;
        }
        while(j>=0){
            int ans=list2[j];
            if( remainder==1){
                ans+=1;
                if(ans>=10){
                    ans%=10;
                    remainder=1;
                }
                else{
                    remainder=0;
                }
                res.push_back(ans);
            }
            else{
                res.push_back(ans);
            }
            j--;
        }
        if(remainder==1){
            res.push_back(1);
        }
        ListNode* newnode=new ListNode(res[0]);
        ListNode* temp2=newnode;
        for(int i=1;i<res.size();i++){
            ListNode* temp1=new ListNode(res[i]);
            newnode->next=temp1;
            newnode=newnode->next;
        }
        return temp2;
    }
};