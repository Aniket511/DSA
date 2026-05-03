class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        hashmap = {}
        stack = []

        for number in reversed(nums2):
            while stack and stack[-1] <= number:
                stack.pop()
            hashmap[number] = -1 if not stack else stack[-1]
            stack.append(number)
        return [hashmap[number] for number in nums1]

solution = Solution()

print(solution.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))