
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {ever_rat(self)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return a

    def __lt__ (self,other):
        if not isinstance(other,Student):
            print('Not a Student')
            return
        return ever_rat(self) < ever_rat(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
     def __init__(self, name, surname):
         self.name = name
         self.surname = surname
         self.courses_attached = []
         self.grades = {}
      
     def __str__(self):
        a = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{ever_rat(self)}'
        return a
     def __lt__ (self,other):
        if not isinstance(other,Lecturer):
            print('Not a Lecturer')
            return
        return ever_rat(self) < ever_rat(other)

class Reviewer(Mentor):
   def __str__(self):
           a = f'Имя: {self.name}\nФамилия: {self.surname}'
           return a

   def rate_hw(self, student, course, grade):
       if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
       else:
            return 'Ошибка'
       
def ever_rat(self):
    s=0
    k=0
    for i in self.grades.values():
        for j in i:
            s += j
            k += 1
    return (s/k)

def ever_rat_student(list_student, course):
    s=0
    k=0
    for i in list_student:
        if course in i.grades:
            for j in i.grades[course]:
                s += j
                k += 1
    if s == 0:
       return f'Не выставлены оценки для студентов за курс {course}'
    else:
       return f'Средняя оценка для студентов за курс {course} составляет {(s/k)}'

def ever_rat_lecturer(list_lecturer, course):
    s=0
    k=0
    for i in list_lecturer:
        if course in i.grades:
            for j in i.grades[course]:
                s += j
                k += 1
    if s == 0:
        return f'Не выставлены оценки для лекторов за курс {course}'
    else:
        return f'Средняя оценка для лекторов за курс {course} составляет {(s/k)}'

student1 = Student('Ruy', 'Eman', 'male')
student1.courses_in_progress = ['Python','Git']
student2 = Student('Anna', 'Ivanova', 'female')
student2.courses_in_progress = ['Python']

Reviewer1 = Reviewer('Petr', 'Petrov')
Reviewer1.courses_attached = ['Python','Git']
Reviewer1.rate_hw(student1, 'Python', 9)
Reviewer1.rate_hw(student1, 'Git', 2)
Reviewer1.rate_hw(student2, 'Python', 5)

Reviewer2 = Reviewer('Jou', 'Buddy')
Reviewer2.courses_attached = ['Python']
Reviewer2.rate_hw(student1, 'Python', 10)
Reviewer2.rate_hw(student2, 'Python', 7)

Lecturer1 = Lecturer('Stiv','Jobs')
Lecturer1.courses_attached = ['Python']
Lecturer2 = Lecturer('Bill','Geits')
Lecturer2.courses_attached = ['Python']

student1.rate_lecturer(Lecturer1, 'Python', 10)
student1.rate_lecturer(Lecturer2, 'Python', 12)
student2.rate_lecturer(Lecturer1, 'Python', 5)
student2.rate_lecturer(Lecturer2, 'Python', 5)

print(student1)
print(student2)
print(student1 < student2)
print(Reviewer1)
print(Reviewer2)
print(Lecturer1)
print(Lecturer2)
print(Lecturer1 < Lecturer2)

print(ever_rat_student([student1,student2],'Python'))
print(ever_rat_lecturer([Lecturer1,Lecturer2],'Python'))
