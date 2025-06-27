class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # Step 1: Sort balloons by their ending x coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1  # we need at least one arrow
        end = points[0][1]  # shoot arrow at the end of first balloon

        for start, xend in points:
            if start > end:
                # New balloon doesn't overlap; shoot a new arrow
                arrows += 1
                end = xend  # update the new arrow's position

        return arrows



