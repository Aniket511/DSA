class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        current_combination = []
        candidates.sort()

        
        def backtrack(start, remaining):
            # Base case 1: We've found a valid combination that sums to target
            if remaining == 0:
                result.append(current_combination[:])  # Add a copy to results
                return
            
            # Base case 2: We've exceeded the target, this path won't work
            # (This is implicit - we stop exploring when remaining becomes negative)
            if remaining < 0:
                return
            
            # Try each candidate starting from 'start' index
            for i in range(start, len(candidates)):
                # Make the choice: include candidates[i]
                current_combination.append(candidates[i])
                
                # THE KEY DIFFERENCE: We pass 'i' (not i+1) to allow reusing the same element
                # We subtract candidates[i] from remaining to track how much we still need
                backtrack(i, remaining - candidates[i])
                
                # Backtrack: undo the choice
                current_combination.pop()
        
        backtrack(0, target)
        return result