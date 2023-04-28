from typing import List
class UnionFind:
    def __init__(self):
        self.father = {}

    def find(self, x):
        if x not in self.father:
            self.father[x] = x
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            return True
        return False


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        uf = UnionFind()
        ans = len(strs)

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                count = 0
                word1, word2 = strs[i], strs[j]
                for k in range(len(word1)):
                    if word1[k] != word2[k]:
                        count += 1
                if count == 2 or count == 0:
                    ans -= uf.union(i, j)
        return ans

