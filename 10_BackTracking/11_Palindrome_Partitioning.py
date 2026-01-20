class Solution:
    def partition(self, s):
        
        result = []
        stack = []

        def isPalindrome(left, right):

            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtracking(idx):

            if idx == len(s):
                result.append(stack[::])
                return

            for j in range(idx, len(s)):
                if isPalindrome(idx, j):
                    stack.append(s[idx : j + 1])
                    backtracking(j + 1)
                    stack.pop()
        
        backtracking(0)

        return result

solution = Solution()
solution.partition('abcba')