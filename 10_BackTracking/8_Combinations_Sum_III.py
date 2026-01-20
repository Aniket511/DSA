class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        current_combination = []
        
        def backtrack(start, remaining, count):
            # Base case 1: We've selected k numbers and they sum to n
            if count == k and remaining == 0:
                result.append(current_combination[:])
                return
            
            # Base case 2: We've selected k numbers but haven't reached target
            # OR we've exceeded the target
            # In either case, this path won't work
            if count == k or remaining <= 0:
                return
            
            # Try each number from start to 9
            for i in range(start, 10):
                # Optimization: if current number exceeds remaining, 
                # all subsequent numbers will too (since we go 1,2,3...9)
                if i > remaining:
                    break
                
                # Make the choice: include number i
                current_combination.append(i)
                
                # Recurse: move to next number (i+1), decrease remaining, increase count
                backtrack(i + 1, remaining - i, count + 1)
                
                # Backtrack: undo the choice
                current_combination.pop()
        
        backtrack(1, n, 0)
        return result

solution = Solution()
print(solution.combinationSum3(size = 3, target = 7))
print(solution.combinationSum3(size = 3, target = 9))