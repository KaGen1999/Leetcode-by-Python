class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0 for _ in range(n)]
        l[0] = nums[0]
        max_sum = l[0]
        for i in range(1, n):
            l[i] = max(l[i - 1] + nums[i], nums[i])
            if l[i] > max_sum:
                max_sum = l[i]
        return max_sum
