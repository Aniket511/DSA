class MyHashSet:

    def __init__(self):
        self.hashSet = [0 for _ in range(31251)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet[key // 32] ^= 1 << (key % 32)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet[key // 32] ^= 1 << (key % 32)

    def contains(self, key: int) -> bool:
        return self.hashSet[key // 32] & 1 << (key % 32) != 0

