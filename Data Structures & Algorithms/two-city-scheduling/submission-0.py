class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0])

        cost = 0
        n = len(costs) // 2

        for i in range(len(costs)):
            if i < n:
                cost += costs[i][1]
            else:
                cost += costs[i][0]
        
        return cost