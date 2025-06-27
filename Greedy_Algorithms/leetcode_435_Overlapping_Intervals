class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        //step1:sorting by end_time
        intervals.sort(key=lambda x: x[1])
        //step2
        prev_end = float('-inf')
        count = 0

        for start, end in intervals:
            if start < prev_end:
                count += 1  // overlap, so remove this one
            else:
                prev_end = end   // no overlap, keep it

        return count

