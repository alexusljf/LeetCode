class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # iterate thru the list while placing flowers (setting 0 to 1)
        # flowers cannot be adjacent (no two 1s adjacent)
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                next = flowerbed[i+1] if i < length - 1 else flowerbed[i]
                prev = flowerbed[i-1] if i > 0 else flowerbed[i]
                if next == 0 and prev == 0:
                    flowerbed[i] = 1
                    count += 1
        return count >= n

