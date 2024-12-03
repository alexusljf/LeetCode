class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)
        for child in candies:
            if (child + extraCandies) >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
        