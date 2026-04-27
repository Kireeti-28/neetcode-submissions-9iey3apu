class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adjList = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattrn = word[:j] + "*" + word[j+1:]
                adjList[pattrn].append(word)
        
        queue = deque([])
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)

        res = 1
        while len(queue) != 0:
            for i in range(len(queue)):
                cur = queue.popleft()

                if cur == endWord:
                    return res

                for j in range(len(cur)):
                    pattrn = cur[:j] + "*" + cur[j+1:]
                    for neighbor in adjList[pattrn]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            
            res += 1
        
        return 0