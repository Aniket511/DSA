class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head
        
        oldToNew = {}

        current = head
        while current:
            oldToNew[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            oldToNew[current].next = oldToNew.get(current.next)
            oldToNew[current].random = oldToNew.get(current.random)
            current = current.next

        return oldToNew[head]


class Solution:
    def copyRandomList(self, head):

        if not head:
            return None

        current = head
        while current:
            newNode = Node(current.val)
            newNode.next = current.next
            current.next = newNode
            current = newNode.next

        current = head
        while current:
            
            newNode = current.next
            if current.random:
                newNode.random = current.random.next
            else:
                newNode.random = None
            current = newNode.next
        
        current = head
        newHead = head.next

        while current:
            copyNode = current.next

            current.next = copyNode.next

            if copyNode.next:
                copyNode.next = copyNode.next.next

            current = current.next

        return newHead