# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        listDict= {}
        for ll in lists:
            temp = ll
            while temp is not None:
                if listDict.get(temp.val) is None:
                    listDict[temp.val] = []
                listDict[temp.val].append(temp)
                temp = temp.next
        keyList = list(listDict.keys())
        keyList.sort()
        startNode = None
        newNode = None
        for key in keyList:
            for node in listDict[key]:
                if newNode is None:
                    newNode = node
                    startNode = node
                else:
                    newNode.next= node
                    newNode = newNode.next
        return startNode

