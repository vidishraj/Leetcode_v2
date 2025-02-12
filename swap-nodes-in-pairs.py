class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        List node is a class with two properties-> val and next.
        """
        if head is None:
            return head
        firstNode = head
        secondNode = firstNode.next
        if secondNode is None:
            return head
        count=0
        trailingNode=None
        while (firstNode is not None):
            # print(firstNode)
            # print(secondNode)
            thirdNode=secondNode.next
            secondNode.next = firstNode
            firstNode.next =thirdNode
            if count==0:
                head=secondNode
                trailingNode=firstNode
            else:
                trailingNode.next=secondNode
                trailingNode=firstNode
            count=+1
            # print(firstNode)
            # print(secondNode)
            firstNode=thirdNode
            if firstNode is None:
                return head
            secondNode=firstNode.next
            if secondNode is None:
                return head
        return head