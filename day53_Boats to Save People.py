class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        n = len(people)
        left, right = 0, n - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        
        return boats
