# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dnq(nums):
            if len(nums) == 2: return TreeNode(nums[1], TreeNode(nums[0]))
            if len(nums) == 1: return TreeNode(nums[0])
            mid = len(nums) // 2

            return TreeNode(nums[mid], dnq(nums[:mid]), dnq(nums[mid + 1:]))

        return dnq(nums)
