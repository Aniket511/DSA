class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        for word in strs:
            frequency = [0] * 26
            for letter in word:
                frequency[ord(letter) - ord("a")] += 1
            if tuple(frequency) not in hashmap:
                hashmap[tuple(frequency)] = [word]
            else:
                hashmap[tuple(frequency)].append(word)
        return list(hashmap.values())