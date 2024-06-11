class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        freq = {}
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for num in arr2:
            if num in freq:
                result.extend([num] * freq.pop(num))

        result.extend(sorted([num for num in freq for _ in range(freq[num])]))

        return result
