import random

class Person:
   def __init__(self, age, name='unknown'):
      self.id = random.randint(1, 1000)
      self.name = name
      self.age = age
      self.parent_permission = age >= 18

   def greet(self):
      print(f"Hello my name is {self.name}, I am {self.age} years old, Fancy meeting you!")

   def has_permission(self):
     return self.parent_permission
