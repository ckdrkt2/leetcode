from collections import defaultdict
from random import random
class RandomizedSet:

    def __init__(self):
        self.d = defaultdict(int)
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.d: return False
        else:
            self.d[val] = len(self.nums)
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.d: return False
        else:
            d_idx = self.d[val]
            self.nums[-1], self.nums[d_idx] = self.nums[d_idx], self.nums[-1]
            self.d[self.nums[d_idx]] = d_idx
            self.d.pop(val)
            self.nums.pop()
            return True

    def getRandom(self) -> int:
        return self.nums[int(random() * len(self.nums))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()