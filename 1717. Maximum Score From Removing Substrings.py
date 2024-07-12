class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        sub1, sub2 = 'ab', 'ba'
        if x < y:
            sub1, sub2 = sub2, sub1
            x, y = y, x

        ans = cnt1 = cnt2 = 0

        for c in s:
            if c == sub1[0]:
                cnt1 += 1
            elif c == sub2[0]:
                if cnt1 > 0:
                    cnt1 -= 1
                    ans += x
                else:
                    cnt2 += 1
            else:
                ans += min(cnt1, cnt2) * y
                cnt1 = cnt2 = 0

        return ans + min(cnt1, cnt2) * y
