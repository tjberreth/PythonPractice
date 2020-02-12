class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        if grade not in self._roster:
            self._roster[grade] = []
        self._roster[grade].append(name)

    def roster(self):
        return [student for grade in sorted(self._roster) for student in sorted(self._roster[grade])]

    def grade(self, grade_number):
        return [] if grade_number not in self._roster else sorted(self._roster[grade_number])
