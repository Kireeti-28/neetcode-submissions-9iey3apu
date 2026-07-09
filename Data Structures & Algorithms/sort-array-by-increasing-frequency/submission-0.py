class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        mp = {}

        for num in nums:
            if num not in mp:
                mp[num] = 1 
            else:
                mp[num] += 1
        
        for key, value in mp.items():
            bucket[value].append(key)
        
        ans = []
        for i in range(len(bucket)):
            if len(bucket[i]) > 0:
                # print(bucket[i], i)
                for j in range(len(bucket[i]) - 1, -1, -1):
                    ans.extend(i * [bucket[i][j]])
        
        return ans
