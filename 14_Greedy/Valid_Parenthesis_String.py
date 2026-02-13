class Solution:
    def checkValidString(self, s: str) -> bool:
        
        minOpenBrackets = 0
        maxOpenBrackets = 0

        for character in s:
            
            if character == '(':
                minOpenBrackets += 1
                maxOpenBrackets += 1
            
            elif character == ')':
                minOpenBrackets -= 1
                maxOpenBrackets -= 1
                 
            else:
                minOpenBrackets -= 1
                maxOpenBrackets += 1

            if maxOpenBrackets < 0:
                return False
            
            if minOpenBrackets < 0:
                minOpenBrackets = 0

        return minOpenBrackets == 0

solution = Solution()
print(solution.checkValidString('()(*)))'))