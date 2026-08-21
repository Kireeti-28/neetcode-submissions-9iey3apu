class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_map = {}

        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        

        lst = []
        for key, value in freq_map.items():
            if key == value:
                lst.append(key)
        
        if lst:
            return max(lst)
        
        return -1