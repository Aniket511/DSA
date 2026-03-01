class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        right = dummy

        for _ in range(n):
            right = right.next

        left = dummy

        while right and right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next