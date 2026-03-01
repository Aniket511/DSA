class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return 

        dummy = ListNode(0, head)
        current = dummy.next

        while current and current.next:
            while current and current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next

        return dummy.next