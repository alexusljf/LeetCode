class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # iterate thru the list while placing flowers (setting 0 to 1)
        # flowers cannot be adjacent (no two 1s adjacent)
        count = 0
        length = len(flowerbed)
        i = 0
        while i <length:
        # for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == len(flowerbed)-1 or flowerbed[i+1] == 0) and (i == 0 or flowerbed[i-1] == 0):
                flowerbed[i] = 1
                count += 1
                i+=1 # to skip over next as impossible
            i += 1 
        return count >= n

