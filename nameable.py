class Nameable:
  def __init__(self):
    raise NotImplementedError(f"{type(self), __name__} has not implemented {self.correct_name, __name__}")