class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current_combination = []
        candidates.sort()  # Critical: sort to group duplicates together
        
        def backtrack(start, remaining):
            # Base case 1: Found a valid combination
            if remaining == 0:
                result.append(current_combination[:])
                return
            
            # Base case 2: Exceeded target (optimization - could omit this)
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # THE KEY DUPLICATE-HANDLING LOGIC:
                # Skip if this element equals the previous element at the same decision level
                # This is identical to the skip condition in Subsets II
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Optimization: if current candidate exceeds remaining, break
                # (all subsequent candidates are also too large since array is sorted)
                if candidates[i] > remaining:
                    break
                
                # Make the choice: include candidates[i]
                current_combination.append(candidates[i])
                
                # THE KEY DIFFERENCE FROM COMBINATION SUM:
                # We pass i+1 (not i) because each element can only be used once
                backtrack(i + 1, remaining - candidates[i])
                
                # Backtrack: undo the choice
                current_combination.pop()
        
        backtrack(0, target)
        return result