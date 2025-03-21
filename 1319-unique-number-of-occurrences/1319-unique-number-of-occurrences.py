class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        print(count, set(count.values()), len(count))
        return (len(set(count.values())) == len(count))