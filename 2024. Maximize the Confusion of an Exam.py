class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, target: int) -> int:
        ans = 0
        for ch in "TF":
            j, k = 0, target
            for i in answerKey:
                if i == ch: k -= 1
                if k < 0:
                    if answerKey[j] == ch: k += 1
                    j += 1
            ans = max(ans, len(answerKey) - j)
        return ans
