class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # lastOccurences = {}
        # for i,char in enumerate(s):
        #     lastOccurences[char] = i
        # partitions = []
        # start,end = 0,0
        # for i,char in enumerate(s):
        #     end = max(end, lastOccurences[char])
        #     if i == end:
        #         partitions.append(i-start+1)
        #         start = i+1
        # return partitions
        
        # merge intervals way of doing
        occurences = {} # store the first and last occurences
        for i, char in enumerate(s):
            if char not in occurences:
                occurences[char] = [i,i]
            else:
                occurences[char][1] = i
        intervals = sorted(occurences.values())
        # init the first interval
        partitions = [intervals[0]]
        for i in range(1,len(intervals)):
            # if cur start is <= last interval's end, then merge
            if intervals[i][0] <= partitions[-1][1]:
                # update the end of the last interval to max of cur and last end
                partitions[-1] = [partitions[-1][0], max(intervals[i][1], partitions[-1][1])]
            else:
                # else add the interval entirely
                partitions.append(intervals[i])
                
        return [end - start + 1 for start,end in partitions]
