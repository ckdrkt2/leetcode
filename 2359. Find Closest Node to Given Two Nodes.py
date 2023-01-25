class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1

        n1, n2 = {node1}, {node2}
        ans = 1000000

        while node1 >= 0 or node2 >= 0:
            e1, e2 = edges[node1], edges[node2]
            if e1 in n1 and e2 in n2: break

            n1.add(e1)
            n2.add(e2)

            if e1 in n2: ans = min(ans, e1)
            if e2 in n1: ans = min(ans, e2)
            if ans < 1000000: return ans
            if e1 != -1: node1 = e1
            if e2 != -1: node2 = e2
        return -1