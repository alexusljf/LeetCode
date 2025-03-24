class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        noMeetings = 0
        # to track the latest end iterated
        latestEnd = 0
        for start, end in meetings:
            # if current start has a gap between previous end, then increment the no meetings
            if start > latestEnd + 1:  
                noMeetings += start - latestEnd - 1
            # update the latest end to be the ending of current iteration
            latestEnd = max(latestEnd, end)
        noMeetings += days - latestEnd
        return noMeetings