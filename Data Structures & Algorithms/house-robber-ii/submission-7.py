class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(houses):
            a = 0
            b = 0

            for n in houses:
                tmp = b
                b = max(n + a, b)
                a = tmp
            
            return b

        return max(solve(nums[:-1]), solve(nums[1:]))