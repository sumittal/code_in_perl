'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_collinear_point_count = 0

        # find unique points
        point_to_count = defaultdict(int)
        for point in points:
            point_to_count[tuple(point)] += 1
        unique_points = list(point_to_count.keys())

        # for each point, check how many other points are on the same lines passing through it
        for i1 in range(len(unique_points)):
            p1 = unique_points[i1]
            slope_to_point_count = defaultdict(int)
            for i2 in range(i1+1, len(unique_points)):
                p2 = unique_points[i2]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]

                slope_tuple = (0, 1)
                if dx != 0:
                    signed_gcd = gcd(dx, dy) * (1 if dx > 0 else -1)
                    slope_tuple = (dx // signed_gcd, dy // signed_gcd)
                slope_to_point_count[slope_tuple] += point_to_count[p2]
            max_collinear_point_count_pass_p1 = max(slope_to_point_count.values(), default=0) + point_to_count[p1]
            max_collinear_point_count = max(max_collinear_point_count, max_collinear_point_count_pass_p1)

        return max_collinear_point_count

        def gcd(self, a, b):
        if a < b:
            a, b = b, a
            
        if b == 0:
            return a
        c = a % b
        return self.gcd(b, c)