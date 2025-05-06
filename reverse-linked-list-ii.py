# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def count(self, head):
        count =0 
        while head is not None:
            count+=1
            head = head.next
        return count

    def reverse(self, head):
        """
        Take Two at a time 
        """
        count = self.count(head)
        if count == 1 :
            return head, head
        if count ==2 :
            # Just swap values
            tmp = head.val
            head.val = head.next.val
            head.next.val = tmp
            return head, head.next
        first = head
        second = first.next
        last = None
        lastRef = head
        while first is not None:
            first.next = last
            if second is None:
                head = first
                break
            last = second.next
            second.next = first
            first = last 
            last = second
            if first is None:
                head = second
                break
            second = first.next 
        return head, lastRef

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = 1
        headC = head
        prevNode = None
        while curr!=left:
            curr+=1
            prevNode = headC
            headC=headC.next
        startNode = headC
        while curr!=right:
            curr+=1
            headC=headC.next
        endNode = headC
        headC = headC.next
        endNode.next = None
            
        reved, lastRef =  self.reverse(startNode)
        if prevNode is not None:
            prevNode.next = reved
        else:
            head = reved
        if lastRef is not None:
            lastRef.next = headC
        return head