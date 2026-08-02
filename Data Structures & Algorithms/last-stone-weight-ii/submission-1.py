class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = math.ceil(stone_sum / 2)
        n = len(stones)

        def tabulation():
            # intialisation table
            dp = [[0] * (target + 1) for _ in range(n + 1)]


        def memoization(i, cur_sum):
            if cur_sum >= target or i >= n:
                return abs(cur_sum - (stone_sum - cur_sum))
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            
            memo[(i, cur_sum)] = min(memoization(i + 1, cur_sum + stones[i]), memoization(i + 1, cur_sum))
            return memo[(i, cur_sum)]
        
        memo= {}
        return memoization(0, 0)