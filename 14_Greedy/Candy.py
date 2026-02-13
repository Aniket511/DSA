class Solution:
    def candy(self, ratings: list[int]) -> int:

        number_of_children = len(ratings)
        candies = 1
        idx = 1
        
        while idx < number_of_children:
            if ratings[idx] == ratings[idx - 1]:
                idx += 1
                candies += 1
                continue
        
            peak = 1
            while idx < number_of_children and ratings[idx] > ratings[idx - 1]:
                peak += 1
                candies += peak
                idx += 1
        
            valley = 1
            while idx < number_of_children and ratings[idx] < ratings[idx - 1]:
                candies += valley
                valley += 1
                idx += 1
        
            if valley > peak:
                candies += valley - peak
        
        return candies

class Solution:
    def candy(self, ratings: list[int]) -> int:
        
        candies = number_of_children = len(ratings)
        idx = 1
        
        while idx < number_of_children:
            if ratings[idx] == ratings[idx - 1]:
                idx += 1
                continue
        
            peak = 0
            while idx < number_of_children and ratings[idx] > ratings[idx - 1]:
                peak += 1
                candies += peak
                idx += 1
        
            valley = 0
            while idx < number_of_children and ratings[idx] < ratings[idx - 1]:
                valley += 1
                candies += valley
                idx += 1
        
            candies -= min(peak, valley)
        
        return candies