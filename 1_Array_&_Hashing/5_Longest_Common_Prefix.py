class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        curr_word = strs[0]
        for idx, letter in enumerate(curr_word):
            for word in strs:
                if idx == len(word) or letter != word[idx]:
                    return word[:idx]
        return curr_word