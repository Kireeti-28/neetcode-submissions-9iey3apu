class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def backtrack(nums_cp, perm):
            if not nums_cp:
                perms.append(perm)
                return

            for i in range(len(nums_cp)):
                nums_new = nums_cp[:i] + nums_cp[i + 1:]
                backtrack(nums_new, perm + [nums_cp[i]])
        
        backtrack(nums[:][:], [])

        return perms
                
