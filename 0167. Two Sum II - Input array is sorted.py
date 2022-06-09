class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target: break
            if s > target: j -= 1
            else: i += 1 
        return [i + 1, j + 1]

'''
time complexity: O(N)
space complexity: O(1)
'''