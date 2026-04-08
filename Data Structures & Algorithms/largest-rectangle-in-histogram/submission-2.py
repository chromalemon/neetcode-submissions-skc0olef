class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maximum = 0
        for index, height in enumerate(heights):
            new_index = index
            while stack and stack[-1][1] > height:
                [prev_index, prev_height] = stack.pop()
                area = prev_height*(index-prev_index)
                maximum = max(maximum, area)
                new_index = min(new_index, prev_index)
            stack.append([new_index, height])
        if stack:
            index = n
            while stack:
                [prev_index, prev_height] = stack.pop()
                area = prev_height*(index-prev_index)
                maximum = max(maximum, area)
        return maximum