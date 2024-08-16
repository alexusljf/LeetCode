class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # initialise min and max values with the first array
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        maxDist = 0
        # start from 2nd array to ensure 2 different arrays are being compared
        for i in range(1, len(arrays)):
            array = arrays[i]
            maxDist = max(maxDist, abs(array[-1] - minVal), abs(maxVal - array[0]))
            minVal = min(minVal, array[0])
            maxVal = max(maxVal, array[-1])
        return maxDist