class Solution:
    def letterCombinations(self, digits):

        result = []
        currentCombination = []

        digit_to_letters = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }

        def backtrack(idx):

            if idx == len(digits):
                result.append(''.join(currentCombination))
                return

            for letter in digit_to_letters[digits[idx]]:
                currentCombination.append(letter)
                backtrack(idx + 1)
                currentCombination.pop()

        backtrack(0)
        return result

solution = Solution()

testCases = ['23', '45', '62', '32', '89', '97']

for idx, digits in enumerate(testCases):
    result = solution.letterCombinations(digits)
    print(f"Test Case {idx + 1}, result {result}:")