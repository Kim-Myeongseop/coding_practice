class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        max_len = len(students)
        delay = 0
        while len(students)>0 and delay<max_len:
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
                delay = 0
                max_len -= 1
            else:
                students.append(students[0])
                students = students[1:]
                delay += 1
        return len(students)