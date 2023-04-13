from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        a = []
        for i in pushed:
            a.append(i)
            while a and a[-1] == popped[0]:
                a.pop()
                popped.pop(0)
        return not a
