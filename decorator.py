from nameable import Nameable

class Decorator(Nameable):
  def __init__(self, nameable):
    super().__init__()
    self.nameable = nameable

  def correct_name(self):
    return self.nameable.correct_name()
