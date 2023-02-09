from typing import List
from string import ascii_lowercase
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        arr = [set() for _ in range(26)]
        for idea in ideas:
            arr[ascii_lowercase.find(idea[0])].add(idea[1:])

        ans = 0
        for i in range(25):
            for j in range(i + 1, 26):
                k = len(arr[i] & arr[j])
                ans += 2 * (len(arr[i]) - k) * (len(arr[j]) - k)
        return ans