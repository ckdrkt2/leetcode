from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        counter = [0] * n
        for node in leftChild:
            if node >= 0: counter[node] += 1
        for node in rightChild:
            if node >= 0: counter[node] += 1

        cnt, root = 0, None
        for i, c in enumerate(counter):
            if c > 1: return False
            if c == 0:
                cnt += 1
                root = i

        if cnt != 1: return False

        seen, stack = set(), [root]
        while stack:
            curr = stack.pop()
            if leftChild[curr] >= 0:
                stack.append(leftChild[curr])
            if rightChild[curr] >= 0:
                stack.append(rightChild[curr])
            seen.add(curr)

        return len(seen) == n
