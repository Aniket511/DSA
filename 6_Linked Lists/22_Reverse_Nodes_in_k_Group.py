class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def hasKNodes(node, k):

            count = 0
            current = node
            while current and count < k:
                current = current.next
                count += 1
            return count == k

        def reverseNodes(node, k):

            previous = None
            current = node

            for _ in range(k):
                nextNode = current.next
                current.next = previous
                previous = current
                current = nextNode
            
            return previous, node, current

        dummy = ListNode(0, head)
        previousTail = dummy

        while hasKNodes(previousTail.next, k):

            newHead, newTail, nextHead = reverseNodes(previousTail.next, k)

            previousTail.next = newHead
            newTail.next = nextHead
            previousTail = newTail

        return dummy.next