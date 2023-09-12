from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        ans, cnt = 0, sorted(Counter(s).values(), reverse=True)
        for i in range(len(cnt) - 1):
            if cnt[i] == 0:
                ans += sum(cnt[i + 1:])
                break
            if cnt[i] <= cnt[i + 1]:
                ans += cnt[i + 1] - cnt[i] + 1
                cnt[i + 1] = cnt[i] - 1
        return ans
