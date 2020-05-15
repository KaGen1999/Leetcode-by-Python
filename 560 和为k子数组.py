class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        count = 0
        s = 0
        for num in nums:
            s = s + num
            if d.get(s - k):
                count = count + d[s - k]
            if d.get(s):
                d[s] = d[s] + 1
            else:
                d[s] = 1

        return count
