class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for idx, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [hashmap[difference], idx]
            hashmap[number] = idx