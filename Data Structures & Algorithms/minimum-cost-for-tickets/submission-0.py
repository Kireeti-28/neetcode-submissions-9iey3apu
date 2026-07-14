class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        lastDay = max(days)

        def dfs(i):
            if i > lastDay:
                return 0
            
            if i not in days:
                return dfs(i + 1)
            
            return min(
            costs[0] + dfs(i + 1),
            costs[1] + dfs(i + 7),
            costs[2] + dfs(i + 30))
        
        firstDay = min(days)
        return dfs(firstDay)