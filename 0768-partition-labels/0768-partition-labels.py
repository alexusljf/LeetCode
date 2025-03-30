class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurences = {}
        for i,char in enumerate(s):
            lastOccurences[char] = i
        partitions = []
        start,end = 0,0
        for i,char in enumerate(s):
            end = max(end, lastOccurences[char])
            if i == end:
                partitions.append(i-start+1)
                start = i+1
        return partitions
            