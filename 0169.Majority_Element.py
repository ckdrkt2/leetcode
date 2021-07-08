class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = None
        c = 0
        for i in nums:
            if c == 0:
                a = i
            c += (1 if i == a else -1)
        return a

# 개수가 절반 이상이기 때문에 majority element가 리스트에서 가장 많음
# 따라서 다른 수의 개수와 majority element의 개수의 차가 항상 양수인 것을 활용