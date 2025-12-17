class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = sorted(candies)[-1]
        bool_array = []
        for candy in candies:
            bool_array.append(candy + extraCandies >= max_candies)

        return bool_array
       