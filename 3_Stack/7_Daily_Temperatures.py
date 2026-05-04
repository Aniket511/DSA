class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        n = len(temperatures)
        result = [0] * (n)

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = n
                    break
                j += result[j]
            if j < n:
                result[i] = j - i
        
        return result

class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        
        result = [0 for _ in range(len(t))]
        stack = []

        for idx, temperature in enumerate(t):
            while stack and t[stack[-1]] < temperature:
                i = stack.pop()
                result[i] = idx - i
            stack.append(idx)
        
        return result