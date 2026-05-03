class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        hashmap = { "(" : ")", "{" : "}", "[" : "]"}

        for b in s:
            if b in hashmap.keys():
                stack.append(b)
            else:
                if stack and hashmap[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
        
        return not stack

solution = Solution()

print(solution.isValid("{[()]}"))
print(solution.isValid("{[(]}"))
print(solution.isValid("{[)]}"))