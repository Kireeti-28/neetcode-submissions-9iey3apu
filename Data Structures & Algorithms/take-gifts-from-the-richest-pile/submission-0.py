class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for gift in gifts:
            heapq.heappush(heap, -1 * gift)
        
        for i in range(k):
            cur = heapq.heappop(heap)
            org_val = -cur
            new_val = int(org_val ** 0.5)
            heapq.heappush(heap, -new_val)
        
        return -sum(heap)