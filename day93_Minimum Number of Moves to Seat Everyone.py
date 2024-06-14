class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
     
        seats.sort()
        students.sort()
        
      
        total_moves = 0
        for seat, student in zip(seats, students):
            total_moves += abs(seat - student)
        
        return total_moves
