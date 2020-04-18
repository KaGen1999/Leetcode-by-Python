# 双指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        max_water = 0
        for _ in range(n):
            c = min(height[j],height[i]) * (j-i)
            if c > max_water:
                max_water = c
            if height[j] >= height[i]:
                i = i + 1
            else:
                j = j - 1
        return max_water