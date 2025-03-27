class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        counterArr = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num, count in counter.items():
            counterArr.append([count, num])
        # python sorts by first element, so sort by count in reverse order
        counterArr.sort(reverse = True)
        res = []
        for i in range(k):
            # append the top k nums in counterArr
            res.append(counterArr[i][1])
        return res

        # heapq method using nLargest
        # count = Counter(nums)
        # runs the nlargest function on count.keys. the count.get method is applied on each key and the top k keys with largest values is returned
        # return heapq.nlargest(k, count.keys(), key=count.get)