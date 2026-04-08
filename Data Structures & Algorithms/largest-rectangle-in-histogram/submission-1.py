class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        INF = float("inf")
        maximum = 0
        for index, height in enumerate(heights):
            min_height_i = INF
            for i in range(index, n):
                min_height_i = min(min_height_i, heights[i])
                area = min_height_i*(i-index+1)
                maximum = max(maximum, area)
            min_height_j = INF
            for j in range(index-1, -1, -1):
                min_height_j = min(min_height_j, heights[j])
                area = min_height_j*(index-j)
                maximum = max(maximum, area)
        return maximum