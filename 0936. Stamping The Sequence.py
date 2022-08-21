class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s, t = len(stamp), len(target)
        count, target, ans = t, list(target), []
        def match(i):
            for j in range(s):
                if target[i + j] != stamp[j] and target[i + j] != '?': return False
            return True
        while count:
            c = 0
            for i in range(t - s + 1):
                if match(i) and target[i : s] != '?' * (s - i):
                    ans.append(i)
                    for j in range(s):
                        if target[i + j] != '?':
                            c += 1
                            target[i + j] = '?'
            if not c: return []
            else: count -= c
        return ans[::-1]