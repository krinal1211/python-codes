class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxLength = 0
        start = 0
        end = 0
        frequency = {}

        while end < n:
            frequency[nums[end]] = frequency.get(nums[end], 0) + 1

            while frequency.get(nums[end], 0) > k:
                frequency[nums[start]] -= 1
                if frequency[nums[start]] == 0:
                    del frequency[nums[start]]
                start += 1

            maxLength = max(maxLength, end - start + 1)
            end += 1

        return maxLength
