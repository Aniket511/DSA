class FreqStack:
    def __init__(self):
        self.array = [[]]
        self.hashmap = {}
    def push(self, val):
        value_count = self.hashmap.get(val, 0) + 1
        if value_count == len(self.array):
            self.array.append([])
        self.hashmap[val] = value_count
        self.array[value_count].append(val)
    def pop(self):
        max_element = self.array[-1].pop()
        self.hashmap[max_element] -= 1
        if not self.array[-1]:
            self.array.pop()
        return max_element