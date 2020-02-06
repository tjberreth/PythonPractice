SAMPLE_CLASS = ['Alice', 'Bob', 'Charlie', 'David',
                'Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANT_DICT = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}

def split_string_by_n(line, n):
    '''
    Splits the line into segments n long
    '''
    if len(line) % n != 0:
        raise Exception(f'Line \"{line}\" cannot be split into equal parts of length {n}')
    return [line[i:i+n] for i in range(0, len(line), n)]

class Garden:
    def __init__(self, 
                diagram,
                students = SAMPLE_CLASS):
        self.student_plants = Garden._parse_student_plants(diagram, students)
    
    @staticmethod
    def _parse_plant_list(plant_first_letters):
        def parse_plant(plant_first_letter):
            return PLANT_DICT[plant_first_letter]
        return list(map(parse_plant, plant_first_letters))

    @staticmethod
    def _parse_student_plants(diagram, students):
        diagram = diagram.upper()
        students.sort()
        student_plants = {}
        rows = diagram.split()
        split_rows = [split_string_by_n(row, 2) for row in rows]
        for student, row1, row2 in zip(students, *split_rows):
            student_plants[student] = Garden._parse_plant_list(row1 + row2)
        return student_plants

    def plants(self, student):
        return self.student_plants[student]