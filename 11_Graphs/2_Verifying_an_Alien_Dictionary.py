class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        
        """
        Verify if words are sorted according to the alien dictionary order.
        
        Strategy: Create a mapping of each character to its position in the alien
        order, then compare each adjacent pair of words using this mapping.
        """
        # Build a map: character -> its position in alien alphabet
        order_map = {character: idx for idx, character in enumerate(order)}
        
        # Check each adjacent pair of words
        for idx in range(len(words) - 1):
            word1, word2 = words[idx], words[idx + 1]
            
            # Compare character by character
            for j in range(min(len(word1), len(word2))):
                # If we find a difference, check if it's in the right order
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False  # word1's character comes after word2's - wrong order
                    break  # This pair is valid, move to next pair
            else:
                # If we exhausted the shorter word without finding a difference,
                # word1 must not be longer than word2 (prefix rule)
                if len(word1) > len(word2):
                    return False
        
        return True

testCases = [
    # Test 1: Basic valid case - clearly sorted
    # Each word starts with a letter that comes before the next word's starting letter
    (
        ["hello", "leetcode"],
        "hlabcdefgijkmnopqrstuvwxyz",
        True
    ),
    
    # Test 2: Basic invalid case - wrong order
    # 'l' comes before 'h' in alien order, so "leetcode" should come before "hello"
    (
        ["leetcode", "hello"],
        "hlabcdefgijkmnopqrstuvwxyz",
        False
    ),
    
    # Test 3: Words with common prefix - valid
    # "app" is a prefix of "apple", and the shorter word comes first (correct)
    (
        ["app", "apple"],
        "abcdefghijklmnopqrstuvwxyz",
        True
    ),
    
    # Test 4: Words with common prefix - invalid
    # "apple" is longer than "app", so "app" should come first, not second
    (
        ["apple", "app"],
        "abcdefghijklmnopqrstuvwxyz",
        False
    ),
    
    # Test 5: Multiple words, all sorted correctly
    # We need to verify each adjacent pair is in order
    (
        ["word", "world", "row"],
        "worldabcefghijkmnpqstuvxyz",
        False  # "world" and "row" are out of order ('o' before 'r' in alien order)
    ),
    
    # Test 6: Single word - always valid
    # With only one word, there's nothing to compare, so it's trivially sorted
    (
        ["word"],
        "abcdefghijklmnopqrstuvwxyz",
        True
    ),
    
    # Test 7: All words identical - valid
    # Identical words are considered to be in correct order
    (
        ["apple", "apple", "apple"],
        "abcdefghijklmnopqrstuvwxyz",
        True
    ),
    
    # Test 8: Empty list - edge case
    # No words means nothing to sort, so it's valid
    (
        [],
        "abcdefghijklmnopqrstuvwxyz",
        True
    ),
    
    # Test 9: Difference appears deep in the words
    # First few characters are the same, need to compare later positions
    (
        ["programming", "programmer"],
        "abcdefghijklmnopqrstuvwxyz",
        True  # "programming" < "programmer" because 'idx' < 'r'
    ),
    
    # Test 10: All words start with same letter
    # Need to check second character, third character, etc.
    (
        ["kuvp", "q"],
        "ngxlkthsjuoqcpavbfdermiywz",
        True  # In this alien order, 'k' comes before 'q'
    ),
    
    # Test 11: Complex alien order
    # The order is completely reversed from normal
    (
        ["zy", "zx"],
        "zyxwvutsrqponmlkjihgfedcba",
        True  # 'y' comes before 'x' in this reversed order
    ),
    
    # Test 12: Tricky prefix case in middle of list
    # Third word is a prefix of second word - should be invalid
    (
        ["abc", "abcd", "abc"],
        "abcdefghijklmnopqrstuvwxyz",
        False  # "abcd" comes before "abc" - wrong order
    ),
    
    # Test 13: Single character words
    # Simple comparison, just checking the alien order directly
    (
        ["a", "b", "c"],
        "cba",
        False  # In order "cba", we need c < b < a, but we have a < b < c
    ),
    
    # Test 14: Valid single character words with alien order
    (
        ["z", "x", "y"],
        "zxy",
        True  # Matches the alien order exactly
    ),
]


solution = Solution()

# Run the tests
print("Running test cases for Alien Dictionary:\n")
for idx, (words, order, expected) in enumerate(testCases, 1):
    result = solution.isAlienSorted(words, order)
    status = "PASS" if result == expected else "FAIL"
    print(f"Test {idx}: {status}")
    print(f"  Words: {words}")
    print(f"  Order: {order}")
    print(f"  Expected: {expected}, Got: {result}")
    if result != expected:
        print(f"  MISMATCH!")
    print()