class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        current_combination = []
        
        def backtrack(start):
            # Base case: we've collected k numbers, so we have a complete combination
            if len(current_combination) == k:
                result.append(current_combination[:])  # Add a copy to results
                return
            
            # Try adding each number from start to n
            for i in range(start, n + 1):
                # Make the choice: include number i
                current_combination.append(i)
                
                # Recursively build the rest of the combination
                # Start from i+1 to ensure we only move forward (no duplicates)
                backtrack(i + 1)
                
                # Backtrack: undo the choice to try other possibilities
                current_combination.pop()
        
        backtrack(1)  # Start with number 1
        return result