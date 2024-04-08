class Solution(object):
    def countStudents(self, students, sandwiches):
        count = 0
        n = len(students)
        i = 0

        while i < n:
            if not students or not sandwiches:
                break

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                i = 0
            else:
                students.append(students.pop(0))
                i += 1

            if i == n:
                count = len(students)
                break
        return count
