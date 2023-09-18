from person import Person

class Teacher(Person):
    def __init__(self, age, name='unknown', specialization=None, parent_permission=True):
      super().__init__(age, name, parent_permission)
      self.specialization = specialization

    def can_use_service(self):
       return True
