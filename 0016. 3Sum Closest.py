class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = 100000, len(nums)
        for i in range(n - 2):
            x = nums[i] + nums[-2] + nums[-1]
            if x < target:
                if abs(x - target) < abs(ans - target):
                    ans = x
                continue
            y = nums[i] + nums[i + 1] + nums[i + 2]
            if y > target:
                if abs(y-target) < abs(ans - target):
                    ans = y
                break
            a, k, e = nums[i], i + 1, n - 1
            while k < e:
                s = nums[k] + nums[e]
                if s == target - a: return target
                if abs(s + a - target) < abs(ans - target):
                    ans = s + a
                if s < target - a:
                    k += 1
                else:
                    e -= 1
        return ans