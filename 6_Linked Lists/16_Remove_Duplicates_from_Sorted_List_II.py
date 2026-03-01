class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        current = dummy

        while current:
            while current.next and current.next.next and current.next.val == current.next.next.val:
                duplicateValue = current.next.val
                while current.next and current.next.val == duplicateValue:
                    current.next = current.next.next

            current = current.next
        
        return dummy.next