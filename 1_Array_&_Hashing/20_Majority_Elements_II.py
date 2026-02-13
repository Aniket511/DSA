class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        candidate_1 = 0 
        candidate_2 = 0 
        count_1 = 0 
        count_2 = 0
        for number in nums:
            if number == candidate_1:
                count_1 += 1
            elif number == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = number
                count_1 += 1
            elif count_2 == 0:
                candidate_2 = number
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1

        count_1 = count_2 = 0
        for number in nums:
            if candidate_1 == number:
                count_1 += 1
            elif candidate_2 == number:
                count_2 += 1
        if count_1 > n // 3:
            result.append(candidate_1)
        if count_2 > n // 3:
            result.append(candidate_2)
        return result