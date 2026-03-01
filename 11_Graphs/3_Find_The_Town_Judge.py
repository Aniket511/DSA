class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        hashmap = {}

        for i, j in trust:
            hashmap[i] = hashmap.get(i, 0) - 1
            hashmap[j] = hashmap.get(j, 0) + 1

        for idx in range(1, n + 1):
            if hashmap.get(idx, 0) == n - 1:
                return idx

        return -1

testCases = [
    # Test 1: Basic valid case - clear judge
    # Person 2 trusts nobody, and persons 1 and 3 both trust person 2
    # This is the simplest valid scenario
    (
        3,  # n = 3 people
        [[1, 3], [1, 2], [3, 2]],  # trust relationships
        2  # person 2 is the judge
    ),
    
    # Test 2: Classic example - person 2 is judge
    # Persons 1 and 3 trust person 2, but person 2 trusts nobody
    # Notice person 1 and 3 also have a trust relationship between them
    (
        3,
        [[1, 2], [3, 2]],
        2
    ),
    
    # Test 3: No judge exists - mutual trust
    # Person 1 and 2 trust each other, so neither can be the judge
    # A judge cannot trust anyone
    (
        2,
        [[1, 2], [2, 1]],
        -1  # no valid judge
    ),
    
    # Test 4: Judge trusts someone - disqualified
    # Person 2 looks like a judge (person 1 trusts them), but person 2
    # trusts person 1, which disqualifies them from being the judge
    (
        2,
        [[1, 2], [2, 1]],
        -1
    ),
    
    # Test 5: Not everyone trusts the potential judge
    # Person 2 is trusted by person 1, and person 2 trusts nobody (good so far)
    # But person 3 doesn't trust person 2, so person 2 can't be the judge
    # The judge must be trusted by ALL other n-1 people
    (
        3,
        [[1, 2]],
        -1
    ),
    
    # Test 6: Single person in town
    # With only one person, they trivially satisfy both conditions:
    # - They trust nobody (there's nobody to trust)
    # - Everyone else trusts them (there is no "everyone else")
    (
        1,
        [],  # no trust relationships possible
        1  # person 1 is the judge
    ),
    
    # Test 7: Two people, one is judge
    # Person 1 trusts person 2, and person 2 trusts nobody
    # This is the minimal valid case with actual trust relationships
    (
        2,
        [[1, 2]],
        2
    ),
    
    # Test 8: Two people, no trust at all
    # Neither person trusts the other, so we can't identify a judge
    # The judge must be trusted by everyone else
    (
        2,
        [],
        -1
    ),
    
    # Test 9: Larger town with clear judge
    # Person 4 is trusted by everyone (1, 2, 3) and trusts nobody
    # This tests that our solution scales beyond tiny examples
    (
        4,
        [[1, 4], [2, 4], [3, 4]],
        4
    ),
    
    # Test 10: Judge candidate trusts one person
    # Person 3 receives trust from persons 1 and 2 (good)
    # But person 3 trusts person 1 (bad - disqualifies them)
    (
        3,
        [[1, 3], [2, 3], [3, 1]],
        -1
    ),
    
    # Test 11: Missing one trust relationship
    # Person 3 should be the judge, but person 2 doesn't trust person 3
    # The judge must have exactly n-1 people trusting them
    (
        4,
        [[1, 3], [3, 4], [4, 3]],
        -1
    ),
    
    # Test 12: Complex valid case
    # Many trust relationships exist among people 1-4, but person 5 is judge
    # Person 5 trusts nobody and everyone (1,2,3,4) trusts person 5
    (
        5,
        [[1, 5], [2, 5], [3, 5], [4, 5], [1, 2], [2, 3], [3, 4]],
        5
    ),
    
    # Test 13: Everyone trusts everyone
    # In a fully connected trust graph, nobody can be the judge
    # because everyone trusts at least one other person
    (
        3,
        [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]],
        -1
    ),
    
    # Test 14: Chain of trust pointing to one person
    # Linear chain: 1->2->3->4, everyone eventually points to 4
    # But person 3 doesn't directly trust person 4 (only indirectly through the chain)
    # For person 4 to be judge, ALL others must trust them directly
    (
        4,
        [[1, 2], [2, 3], [3, 4]],
        -1
    ),
    
    # Test 15: Correct linear trust converging on judge
    # Everyone directly trusts person 4, plus some additional relationships
    # Person 4 trusts nobody, so person 4 is the valid judge
    (
        4,
        [[1, 4], [2, 4], [3, 4], [1, 2], [2, 3]],
        4
    ),
    
    # Test 16: Large n, person 1 is judge
    # Testing that the judge can be any person, not necessarily the highest number
    # All of persons 2-10 trust person 1, and person 1 trusts nobody
    (
        10,
        [[2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],
        1
    ),
]

solution = Solution()

# Run tests with both solutions
print("Testing Find the Town Judge:\n")
print("=" * 60)

for i, (n, trust, expected) in enumerate(testCases, 1):
    result = solution.findJudge(n, trust)
    
    status = "Pass" if result == expected else "Fail"
    
    print(f"Test {i}: {status} (Count)")
    print(f"  n = {n}, trust relationships = {len(trust)}")
    print(f"  Expected: {expected}")
    print(f"  Result: {result}")
    
    if result != expected:
        print(f"  MISMATCH - Review this case!")
        print(f"  Trust relationships: {trust}")
    print()