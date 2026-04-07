class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            heapq.heappush_max(heap, [counts[num], num])
        repeat = k
        res = []
        while repeat > 0:
            count, num = heapq.heappop_max(heap)
            if counts[num] == count:
                res.append(num)
                repeat -= 1
        return res