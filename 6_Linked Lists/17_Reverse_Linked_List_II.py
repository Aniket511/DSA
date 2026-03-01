class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(node, k):

            current = node
            previous = None

            for _ in range(k):
                nextNode = current.next
                current.next = previous
                previous = current
                current = nextNode

            return previous, node, current

        dummy = ListNode(0, head)
        previousNode = dummy

        for _ in range(left - 1):
            previousNode = previousNode.next
        
        newHead, newTail, nextHead = reverse(previousNode.next, right - left + 1)

        previousNode.next = newHead
        newTail.next = nextHead

        return dummy.next