from person import Person
from classroom import Classroom

class Student(Person):
  def __init__(self, age, name='unknown', parent_permission=True, classroom=None):
    super().__init__(age, name)
    self.parent_permission = parent_permission
    self.classroom = classroom

  def set_classroom(self, classroom):
    if self.classroom == classroom:
      return
    
    if self.classroom is not None:
      self.classroom.students.remove(self)
    
    self.classroom = classroom

    if self.classroom is not None:
      self.classroom.students.append(self)


  def play_hooky(self):
    return '¯\\(ツ)/¯'