class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = {0 : 1}
        current_sum = count = 0
        for number in nums:
            current_sum += number
            difference = current_sum - k
            count += prefix_sum.get(difference, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return count, prefix_sum

solution = Solution()
print(solution.subarraySum([1,3,-5,7,-2,5,8,-9], 4))