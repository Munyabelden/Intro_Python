class Classroom:
  def __init__(self, label):
    self.label = label
    self.students = []

  def add_student(self, student):
    self.students.append(student)
    student.classroom = self
