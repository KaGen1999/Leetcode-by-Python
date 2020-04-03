class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        s = 0
        for i in range(1,n-1):
            left = height[0:i]
            right = height[i+1:]
            lmax = max(left)
            rmax = max(right)
            if lmax > height[i] and rmax >height[i]:
                d = min(lmax,rmax)-height[i]
                s = s + d
        return s