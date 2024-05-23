from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        n, subsets = len(nums), []

        for i in range(n):
            valids, cur = [{nums[i]}], nums[i]

            for j in range(i):
                if nums[j] == cur + k:
                    continue

                for subset in subsets[j]:
                    if cur + k in subset:
                        continue
                    tmp = set(subset)
                    tmp.add(cur)
                    valids.append(tmp)
            subsets.append(valids)

        return sum([len(subset) for subset in subsets])
