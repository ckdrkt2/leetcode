class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.match_count = 0
        self.distance = distance
        self.recurseIntoChildren(root)
        return self.match_count

    def recurseIntoChildren(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [1]

        left_node_list = self.recurseIntoChildren(node.left)
        right_node_list = self.recurseIntoChildren(node.right)

        left_node_list.sort()
        right_node_list.sort()
        for left_dist in left_node_list:
            for right_dist in right_node_list:
                if left_dist + right_dist > self.distance:
                    break
                self.match_count += 1

        ans = []
        for i in left_node_list:
            ans.append(i+1)
        for i in right_node_list:
            ans.append(i+1)

        return ans
