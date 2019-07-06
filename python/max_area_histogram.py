'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

It is more natural to think about this way. Let left[i] to indicate how many bars to the left (including the bar at index i) 
are equal or higher than bar[i], right[i] is that to the right of bar[i], so the the square of the max rectangle containing bar[i] 
is simply height[i] * (left[i] + right[i] - 1)
'''


def largestRectangleArea(height):
    n = len(height)

    # left[i], right[i] represent how many bars are >= than the current bar

    left = [1] * n
    right = [1] * n
    max_rect = 0

    # calculate left
    for i in range(0, n):
        j = i - 1
        while j >= 0:
            if height[j] >= height[i]:
                left[i] += left[j]
                j -= left[j]
            else:
                break

    print(left)
    # calculate right
    for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n:
            if height[j] >= height[i]:
                right[i] += right[j]
                j += right[j]
            else:
                break

    for i in range(0, n):
        max_rect = max(max_rect, height[i] * (left[i] + right[i] - 1))

    return max_rect

print(largestRectangleArea([2,1,5,6,2,3]))