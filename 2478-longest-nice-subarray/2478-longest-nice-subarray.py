class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # maxLength = 1
        # for i in range(len(nums)):
        #     print(f'current i: {i}')
        #     tempList = [nums[i]]
        #     for j in range(i+1,len(nums)):
        #         print(f'current j: {j}, the bitwise and is {tempList[-1] & nums[j]}')
        #         # append the number if every pair bitwise and returns 0
        #         canAdd = True
        #         # this loop checks if the current num & the other nums in tempList == 0
        #         for num in tempList:
        #             if num & nums[j] !=0:
        #                 canAdd = False
        #                 break
        #         if canAdd:
        #             tempList.append(nums[j])
        #             print(f'tempList appended: {tempList}')
        #         # else reset the tempList
        #         else:
        #             break
        #     maxLength = max(maxLength, len(tempList))
        # return maxLength

        # above solution is O(n^3), use sliding window for O(n)

        left = 0
        maxLength = 1
        runningOR = 0 # used to track the set bits in the window.

        for right in range(len(nums)):
            # runningOR & nums[right] returns 0 if nums[right] has no matching bits. This is == to nums[right] & every number in the window
            while runningOR & nums[right] != 0:
                # XOR to remove the set bits by the nums[left] and increment the counter
                runningOR ^= nums[left]
                left += 1

            # when the & returns 0, we | the num to the window
            runningOR |= nums[right]
            maxLength = max(maxLength, right - left + 1)

        return maxLength