class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = []
        while len(res) < len(s):
            maxIdx = freq.index(max(freq))
            char = chr(maxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] -= 1
            if freq[maxIdx] == 0:
                continue

            tmp = freq[maxIdx]
            freq[maxIdx] = float("-inf")
            nextMaxIdx = freq.index(max(freq))
            char = chr(nextMaxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] = tmp
            freq[nextMaxIdx] -= 1

        return ''.join(res)


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        max_idx = freq.index(max(freq))
        max_freq = freq[max_idx]
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = [''] * len(s)
        idx = 0
        max_char = chr(max_idx + ord('a'))

        while freq[max_idx] > 0:
            res[idx] = max_char
            idx += 2
            freq[max_idx] -= 1

        for i in range(26):
            while freq[i] > 0:
                if idx >= len(s):
                    idx = 1
                res[idx] = chr(i + ord('a'))
                idx += 2
                freq[i] -= 1

        return ''.join(res)