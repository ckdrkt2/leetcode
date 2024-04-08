from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefer = [students.count(0), students.count(1)]
        q_students, q_sandwiches = deque(students), deque(sandwiches)

        while q_students:
            if prefer[q_sandwiches[0]] == 0: break

            if q_students[0] == q_sandwiches[0]:
                prefer[q_sandwiches.popleft()] -= 1
                q_students.popleft()
            else:
                q_students.append(q_students.popleft())

        return len(q_students)
