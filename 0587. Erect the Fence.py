class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def compare_slopes(p1, p2, p3):
            return (p3[1] - p2[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p2[0])

        upper, lower = [], []
        for point in sorted(trees):
            while len(lower) >= 2 and compare_slopes(lower[-2], lower[-1], point) < 0: lower.pop()
            while len(upper) >= 2 and compare_slopes(upper[-2], upper[-1], point) > 0: upper.pop()
            lower.append(tuple(point))
            upper.append(tuple(point))
        return list(set(lower + upper))