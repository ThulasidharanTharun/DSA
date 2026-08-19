class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        # No students
        if not self.students:
            self.students.append(0)
            return 0

        best_seat = 0
        best_dist = self.students[0]

        # Check gaps between students
        for i in range(1, len(self.students)):
            left = self.students[i - 1]
            right = self.students[i]

            seat = (left + right) // 2
            dist = seat - left

            if dist > best_dist:
                best_dist = dist
                best_seat = seat

        # Check the last gap
        last_dist = self.n - 1 - self.students[-1]

        if last_dist > best_dist:
            best_seat = self.n - 1

        self.students.append(best_seat)
        self.students.sort()

        return best_seat

    def leave(self, p: int) -> None:
        self.students.remove(p)
 
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)