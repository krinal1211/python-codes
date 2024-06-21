class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        
        if m == 2:
            return position[-1] - position[0]
            
        def can(min_force):
            count = 1 
            last_pos = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_force:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False

        left = 1
        right = position[-1] - position[0]

        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1
        return left

