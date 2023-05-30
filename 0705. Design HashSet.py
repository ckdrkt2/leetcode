class MyHashSet:

    def __init__(self):
        self.table = [[] for _ in range(2**15)]

    def add(self, key: int) -> None:
        t = key % 2**15
        if key not in self.table[t]:
            self.table[t].append(key)

    def remove(self, key: int) -> None:
        t = key % 2**15
        if key in self.table[t]:
            self.table[t].remove(key)

    def contains(self, key: int) -> bool:
        t = key % 2**15
        return key in self.table[t]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)