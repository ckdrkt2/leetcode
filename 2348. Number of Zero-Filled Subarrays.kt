class Solution {
    fun zeroFilledSubarray(nums: IntArray): Long {
        var ans: Long = 0
        var cnt: Long = 0
        for (n in nums) {
            if (n == 0) cnt += 1
            else cnt = 0
            ans += cnt
        }
        return ans
    }
}