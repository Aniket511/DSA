class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head or not head.next:
            return head

        stack = []
        current = head

        while current:
            stack.append(current)
            current = current.next

        left = 0
        right = len(stack) - 1

        while left < right:
            stack[left].next = stack[right]
            left += 1
            
            if left >= right:
                break
            

            stack[right].next = stack[left]
            right -= 1
        
        stack[left].next = None

        return stack[0]