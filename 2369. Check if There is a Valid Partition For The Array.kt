class Solution {
    fun validPartition(nums: IntArray): Boolean {
        val dp = booleanArrayOf(true, false, nums[0] == nums[1])
        for (i in 2 until nums.size) {
            val cur = if (nums[i] == nums[i - 1] && dp[1]) {
                true
            } else if (nums[i] == nums[i - 1] && nums[i - 1] == nums[i - 2] && dp[0]) {
                true
            } else if (nums[i] - nums[i - 1] == 1 && nums[i - 1] - nums[i - 2] == 1 && dp[0]) {
                true
            } else {
                false
            }
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = cur
        }
        return dp[2]
    }
}