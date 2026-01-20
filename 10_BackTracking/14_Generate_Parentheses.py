class Solution:
    def generateParenthesis(self, n):

        result = []
        current = []
        
        def backtracking(openBrackets, closedBrackets):
            if openBrackets == closedBrackets == n:
                result.append(''.join(current))
                return
            
            if openBrackets < n:
                current.append('(')
                backtracking(openBrackets + 1, closedBrackets)
                current.pop()
            
            if openBrackets > closedBrackets:
                current.append(')')
                backtracking(openBrackets, closedBrackets + 1)
                current.pop()
        
        backtracking(0, 0)
        return result

solution = Solution()
print(solution.generateParenthesis(n = 4))