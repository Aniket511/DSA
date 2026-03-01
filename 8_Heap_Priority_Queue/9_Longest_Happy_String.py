class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = [a, b, c]
        res = []

        def getMax(repeated):
            idx = -1
            maxCnt = 0
            for i in range(3):
                if i == repeated or count[i] == 0:
                    continue
                if maxCnt < count[i]:
                    maxCnt = count[i]
                    idx = i
            return idx

        repeated = -1
        while True:
            maxChar = getMax(repeated)
            if maxChar == -1:
                break
            res.append(chr(maxChar + ord('a')))
            count[maxChar] -= 1
            if len(res) > 1 and res[-1] == res[-2]:
                repeated = maxChar
            else:
                repeated = -1

        return ''.join(res)


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
                heapq.heappush(maxHeap, (count, char))
            else:
                res += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))

        return res


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def rec(max1, max2, max3, char1, char2, char3):
            if max1 < max2:
                return rec(max2, max1, max3, char2, char1, char3)
            if max2 < max3:
                return rec(max1, max3, max2, char1, char3, char2)
            if max2 == 0:
                return [char1] * min(2, max1)

            use1 = min(2, max1)
            use2 = 1 if max1 - use1 >= max2 else 0
            res = [char1] * use1 + [char2] * use2
            return res + rec(max1 - use1, max2 - use2, max3, char1, char2, char3)

        return ''.join(rec(a, b, c, 'a', 'b', 'c'))