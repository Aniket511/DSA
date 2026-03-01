class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        # Phase 1: Detect cycle
        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]    # move 2 steps

            if slow == fast:
                break

        # Phase 2: Find entrance of the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


"""
===================== EXPLANATION (FOR FUTURE REFERENCE) =====================

Problem:
- Array size = n + 1
- Values are in the range [1, n]
- Exactly one number is duplicated (may repeat more than twice)
- No array modification allowed
- O(1) extra space required

Core Idea:
- Treat the array as a linked list
- Each index points to nums[index]
- A duplicate value creates a cycle
- The entry point of the cycle is the duplicate number

---------------------------------------------------------------------------
EXAMPLE WALKTHROUGH
---------------------------------------------------------------------------

Example:
nums = [1, 3, 4, 2, 2]

Index → Value mapping:
0 → 1
1 → 3
3 → 2
2 → 4
4 → 2   ← cycle starts here

Linked list form:
0 → 1 → 3 → 2 → 4
            ↑     |
            └─────┘

Duplicate number = 2

---------------------------------------------------------------------------
PHASE 1: Detect the cycle
---------------------------------------------------------------------------

Initial:
slow = nums[0] = 1
fast = nums[0] = 1

Step 1:
slow = nums[1] = 3
fast = nums[nums[1]] = nums[3] = 2

Step 2:
slow = nums[3] = 2
fast = nums[nums[2]] = nums[4] = 2

slow == fast → cycle detected

---------------------------------------------------------------------------
PHASE 2: Find the entrance of the cycle
---------------------------------------------------------------------------

Reset slow:
slow = nums[0] = 1
fast = 2

Step 1:
slow = nums[1] = 3
fast = nums[2] = 4

Step 2:
slow = nums[3] = 2
fast = nums[4] = 2

slow == fast → entrance of cycle found

---------------------------------------------------------------------------
FINAL ANSWER:
Duplicate number = 2

---------------------------------------------------------------------------
WHY THIS WORKS:
- The duplicate causes two indices to point to the same value
- This guarantees a cycle (Pigeonhole Principle)
- Floyd’s algorithm finds the cycle entrance efficiently

Time Complexity: O(n)
Space Complexity: O(1)
Array Modification: Not allowed (satisfied)

==============================================================================
"""