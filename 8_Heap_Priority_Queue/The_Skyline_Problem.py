from typing import List
from collections import defaultdict
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        sortedHeights = []

        for left, right, height in buildings:
            sortedHeights.append((left, -height))
            sortedHeights.append((right, height))

        sortedHeights.sort()

        result = []

        maxHeap = [0]
        activeHeights = {}
        activeHeights[0] = 1
        
        prevHeight = 0

        for x, height in sortedHeights:

            if height < 0:
                heapq.heappush(maxHeap, height)
                activeHeights[-height] = activeHeights.get(-height, 0) + 1
            else:
                activeHeights[height] -= 1

            while maxHeap and activeHeights[-maxHeap[0]] == 0:
                heapq.heappop(maxHeap)

            currHeight = -maxHeap[0]

            if currHeight != prevHeight:
                result.append([x, currHeight])
                prevHeight = currHeight

        return result

solution = Solution()
print(solution.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(solution.getSkyline(buildings = [[0,2,3],[2,5,3]]))