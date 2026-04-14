"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        prev = 0

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[prev].end:
                return False
            
            prev = i

        return True