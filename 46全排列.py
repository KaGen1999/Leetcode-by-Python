import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def get_p(r, nums):
            if nums == []:
                result.append(copy.copy(r))
                return
            for i in range(len(nums)):
                last_n = nums[i]
                nums.remove(last_n)
                r.append(last_n)
                get_p(r, nums)
                nums.insert(i, last_n)
                r.pop()

        get_p([], nums)
        return result