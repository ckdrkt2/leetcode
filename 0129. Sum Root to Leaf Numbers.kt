/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun sumNumbers(root: TreeNode?): Int {
        return dfs(0, root)
    }
    fun dfs(num: Int, root: TreeNode?): Int {
        if (root == null) return 0
        var num = (num * 10) + root.`val`
        if (root.left == null && root.right == null) return num
        return dfs(num, root.left) + dfs(num, root.right)
    }
}