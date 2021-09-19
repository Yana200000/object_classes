from functools import reduce

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        length = len(self.grades.values())
        count = 0
        for value in self.grades.values():
            for val in value:
                count += val
                average_mark = count / length
                courses_in_progress = ', '.join(self.courses_in_progress)
                finished_courses = ', '.join(self.finished_courses)
                return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_mark}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

    def compare_student(self, another_student):
        if isinstance(another_student, Student):
            length1 = len(self.grades.values())
            length2 = len(another_student.grades.values())
            count1 = 0
            for value1 in self.grades.values():
                for val1 in value1:
                    count1 += val1
                    average_mark1 = count1 / length1
            count2 = 0
            for value2 in another_student.grades.values():
                for val2 in value2:
                    count2 += val2
                    average_mark2 = count2 / length2
            if average_mark1 > average_mark2:
                return 'Средняя оценка за домашнии задания лучше у 1 студента'
            else:
                return 'Средняя оценка за домашнии задания лучше у 2 студента'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_assessed(self, lecturer, student, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] = [grade]
                return lecturer.grades
            else:
                return 'Ошибка'

    def __str__(self):
        length = len(self.grades.values())
        count = 0
        for value in self.grades.values():
            for val in value:
                count += val
                average_mark = count / length
                return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_mark}'

    def compare_lecturer(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            length1 = len(self.grades.values())
            length2 = len(another_lecturer.grades.values())
            count1 = 0
            for value1 in self.grades.values():
                for val1 in value1:
                    count1 += val1
                    average_mark1 = count1 / length1
            count2 = 0
            for value2 in another_lecturer.grades.values():
                for val2 in value2:
                    count2 += val2
                    average_mark2 = count2 / length2
            if average_mark1 > average_mark2:
                return 'Средняя оценка за лекции лучше у 1 лектора'
            else:
                return 'Средняя оценка за лекции лучше у 2 лектора'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] = [grade]
                return student.grades
            else:
                return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_hw(students, course):
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grades = []
            for student in students:
                grades.append(student.grades[course])
            grade = []
            for i in grades:
                grade.append(i[0])
            sum1 = sum(grade)
            length1 = len(grade)
            average_hw_mark = sum1 / length1
            return average_hw_mark

def average_lecturs(lecturer, course):
    for lecturers in lecturer:
        if isinstance(lecturers, Lecturer) and course in lecturers.courses_attached:
            grades = []
            for lecturers in lecturer:
                grades.append(lecturers.grades[course])
            grade = []
            for i in grades:
                grade.append(i[0])
            sum1 = sum(grade)
            length1 = len(grade)
            average_lc_mark = sum1 / length1
            return average_lc_mark

#Студенты
peter = Student("Peter", "Parker", "man")
peter.finished_courses.append('Literature')
#print(peter.finished_courses)
peter.courses_in_progress.append('Russian')
peter.courses_in_progress.append('History')
#print(peter.courses_in_progress)
peter.grades['Russian'] = [9]
#print(peter.grades)

john = Student("John", "Parker", "man")
john.finished_courses.append('History')
#print(john.finished_courses)
john.courses_in_progress.append('Russian')
#print(john.courses_in_progress)
john.grades['History'] = [10]
john.grades['Russian'] = [6]
#print(john.grades)


#Проверяющие
alexander = Reviewer('Alexander', 'Mor')
alexander.courses_attached.extend(['Russian', 'Math'])
#print(alexander.courses_attached)
rechal = Reviewer('Rechal', 'Pul')
rechal.courses_attached.extend(['Russian'])
#print(rechal.courses_attached)

#Лекторы
boris = Lecturer("Boris", "Kim")
boris.grades['Russian'] = [9]
#print(boris.grades)
boris.courses_attached.append('Russian')
#print(boris.courses_attached)
bob = Lecturer("Bob", "Kur")
bob.grades['Russian'] = [10]
#print(bob.grades)
bob.courses_attached.append('Russian')
#print(bob.courses_attached)

print(average_hw([peter, john], 'Russian'))
print(average_lecturs([boris, bob], 'Russian'))