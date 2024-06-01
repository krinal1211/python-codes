class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXOR = [0] * n
        prefixXOR[0] = arr[0]
    
        for i in range(1, n):
            prefixXOR[i] = prefixXOR[i-1] ^ arr[i]
    
        count = 0
    
        for i in range(n):
            for k in range(i+1, n):
                if i == 0:
                    if prefixXOR[k] == 0:
                        count += (k - i)
                else:
                    if prefixXOR[i-1] == prefixXOR[k]:
                        count += (k - i)
    
        return count
