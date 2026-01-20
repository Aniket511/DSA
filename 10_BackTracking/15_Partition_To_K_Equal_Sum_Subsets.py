class Solution:
    def canPartitionKSubsets(self, nums, k):

        totalSum = sum(nums)
        if totalSum % k != 0:
            return False
        
        target = totalSum // k
        nums.sort(reverse = True)
        if nums[0] > target:
            return False

        used = [False for _ in range(len(nums))]

        def backtracking(currentIdx, k, currentSum):

            if k == 0:
                return True

            if currentSum == target:
                return backtracking(0, k - 1, 0)

            for idx in range(currentIdx, len(nums)):
                if used[idx] or currentSum + nums[idx] > target:
                    continue

                used[idx] = True

                if backtracking(idx + 1, k, currentSum + nums[idx]):
                    return True

                used[idx] = True
                if currentSum == 0:
                    return False
            
            return False

        return backtracking(0, k, 0)

solution = Solution()
print(solution.canPartitionKSubsets([1,2,3,4,5,6,7,8], 4))
print(solution.canPartitionKSubsets([19, 18, 14, 6, 6], 3))