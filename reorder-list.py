class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        # Corner case
        stack = []
        if head is None:
            return head
        runner: ListNode = head
        while runner is not None:
            stack.append(runner)
            runner = runner.next
        runsize = int(len(stack)/2)
        removed = 0
        while removed<runsize:
            lastItem = stack.pop()
            removed+=1
            nextItem = head.next
            head.next = lastItem
            lastItem.next = nextItem
            head = nextItem
        if head:
            head.next= None
        return