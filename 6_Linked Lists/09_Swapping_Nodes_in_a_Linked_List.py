class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        firstNode = dummy
        for _ in range(k):
            firstNode = firstNode.next

        secondNode = head
        lastNode = firstNode

        while lastNode and lastNode.next:
            secondNode = secondNode.next
            lastNode = lastNode.next
        
        firstNode.val, secondNode.val = secondNode.val, firstNode.val

        return dummy.next