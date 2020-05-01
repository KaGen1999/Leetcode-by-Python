class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def get_p(r, nums):
            used = []
            if nums == []:
                result.append(r[:])
                return
            for i in range(len(nums)):
                last_n = nums[i]
                if last_n in used:
                    continue
                nums.remove(last_n)
                r.append(last_n)
                used.append(last_n)
                get_p(r, nums)
                nums.insert(i, last_n)
                r.pop()

        get_p([], nums)
        return result