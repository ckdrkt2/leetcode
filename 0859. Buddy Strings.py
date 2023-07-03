class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal:
            chars = set()
            for c in s:
                if c in chars: return True
                chars.add(c)
            return False

        diff = []
        for a, b in zip(s, goal):
            if a != b:
                diff.append([a, b])
                if len(diff) > 2: return False
        if len(diff) == 2 and diff[0] == diff[1][::-1]: return True
        return False
