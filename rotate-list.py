# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # We will try to do it in place 
        count = 0 
        if head is None or k==0:
            return head
        tempHead = head
        lastNode = tempHead
        while tempHead is not None:
            lastNode = tempHead
            tempHead = tempHead.next
            count+=1
        if  count == 0 or count==1:
            return head
        position = k % count 
        if position == 0:
            return head
        position = count - position 
        curr = 0 
        headCpy = head
        prevNode = headCpy
        while position!=curr:
            curr+=1
            prevNode = headCpy
            headCpy = headCpy.next
        prevNode.next = None
        lastNode.next = head
        return headCpy