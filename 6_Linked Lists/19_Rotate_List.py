class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        left = head
        right = head
        
        length = 1
        while right.next:
            right = right.next
            length += 1
        
        k %= length

        if k == 0:
            return head

        right.next = left

        for _ in range(length - k):
            left = left.next
            right = right.next
        
        right.next = None

        return left