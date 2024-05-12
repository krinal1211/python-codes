import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        n = len(quality)
        workers = sorted([(float(wage[i]) / quality[i], quality[i]) for i in range(n)])

        min_cost = float('inf')
        total_quality = 0
        max_heap = []

        for ratio, q in workers:
            total_quality += q
            heapq.heappush(max_heap, -q)

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                min_cost = min(min_cost, total_quality * ratio)

        return min_cost

