class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        maximum_weight = max(people)
        weight_frequency = [0 for _ in range(maximum_weight + 1)]
        
        for weight in people:
            weight_frequency[weight] += 1
        
        print(weight_frequency)
        
        people_idx = 0
        weight_idx = 1
        
        while people_idx < len(people):
            while weight_frequency[weight_idx] == 0:
                weight_idx += 1
            while weight_frequency[weight_idx] > 0:
                people[people_idx] = weight_idx
                weight_frequency[weight_idx] -= 1
                people_idx += 1
        
        print(people)

        number_of_boats = 0
        left = 0
        right = len(people) - 1
        
        while left <= right:
            remaining_weight = limit - people[right]
            right -= 1
            number_of_boats += 1
            if left <= right and remaining_weight >= people[left]:
                left += 1
        return number_of_boats

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        people.sort()

        left = 0
        right = len(people) - 1
        numberOfBoats = 0

        while left <= right:
            remainingWeight = limit - people[right]
            right -= 1
            numberOfBoats += 1
            if left <= right and remainingWeight >= people[left]:
                left += 1
        
        return numberOfBoats

solution = Solution()
print(solution.numRescueBoats(people = [1,3,2,3,2], limit = 3))
print(solution.numRescueBoats(people = [5,1,4,2], limit = 6))