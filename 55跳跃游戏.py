class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return True
        max_d = nums[0]
        for i in range(1,n-1):
            if max_d < i:
                return False
            max_d = max(nums[i]+i,max_d)
        return max_d >= n-1