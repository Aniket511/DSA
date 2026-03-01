class Node:

    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.previous = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.previous = self.left

    def add(self, node):

        previousNode = self.left
        nextNode = self.left.next
        previousNode.next = node
        node.previous = previousNode
        node.next = nextNode
        nextNode.previous = node

    def remove(self, node):

        previousNode = node.previous
        nextNode = node.next
        previousNode.next = nextNode
        nextNode.previous = previousNode
    
    def get(self, key):

        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.capacity:
            lruNode = self.right.previous
            self.remove(lruNode)
            del self.cache[lruNode.key]