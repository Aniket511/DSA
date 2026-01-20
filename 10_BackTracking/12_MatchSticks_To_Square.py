class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:

        totalLength = sum(matchsticks)
        if totalLength % 4 != 0:
            return False
        
        length = totalLength // 4
        matchsticks.sort(reverse= True)
        if matchsticks[0] > length:
            return False

        sides = [0 for _ in range(4)]

        def backtracking(idx):
            if idx == len(matchsticks):
                return True
            for side in range(4):
                if sides[side] + matchsticks[idx] <= length:
                    sides[side] += matchsticks[idx]
                    if backtracking(idx + 1):
                        return True
                    sides[side] -= matchsticks[idx]
                if sides[side] == 0:
                    return False
            return False

        return backtracking(0)

solution = Solution()
print(solution.makesquare([1,1,2,2,2]))
print(solution.makesquare([3,3,3,3,4]))