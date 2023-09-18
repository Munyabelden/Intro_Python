class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.rentals = []

  def to_dict(self):
    return {
      'title': self.title,
      'author': self.author,
      'rentals': [rental.to_dict() for rental in self.rentals]
    }

  def add_rental(self, person, date):
    rental = Rental(date, self, person)
    self.rentals.append(rental)
    return rental
