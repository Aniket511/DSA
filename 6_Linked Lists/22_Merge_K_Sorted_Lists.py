# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(list1, list2):

            dummy = ListNode()
            current = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            
            if list1:
                current.next = list1
            elif list2:
                current.next = list2
            
            return dummy.next

        def divide(left, right):

            if left == right:
                return lists[left]

            middle = (right + left) // 2

            firstGroup = divide(left, middle)
            secondGroup = divide(middle + 1, right)

            return merge(firstGroup, secondGroup)

        if len(lists) < 1 :
            return None

        return divide(0, len(lists) - 1)