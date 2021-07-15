class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {i:None for i in range(-1000,1001)}
        for i, n in enumerate(numbers):
            if target - n >1000 or target - n < -1000:
                continue
            if a[target - n] != None:
                return [a[target - n]+1, i+1]
            else:
                a[n] = i