class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        current = dummy

        while current.next and current.next.next:

            firstNode = current.next
            secondNode = firstNode.next

            firstNode.next = secondNode.next
            current.next = secondNode
            secondNode.next = firstNode

            current = firstNode
        
        return dummy.next