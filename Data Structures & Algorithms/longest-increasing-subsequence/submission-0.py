class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        [9 1 4 2 3 3 7]
        [1 1 1 1 1 1 1]
        [1 1 2 2 3 3 4]
        '''
        lis = [1] * len(nums)
        print(lis)
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                lis[i] = lis[i - 1] + 1
            else:
                lis[i] = max(lis[i - 1], lis[i])
            
            print(lis)
        
        return lis[len(nums) - 1]
            