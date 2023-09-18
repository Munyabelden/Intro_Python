class Rental:
  def __init__(self, date, book, person):
    self.date = date
    self.book = book
    self.person = person

  def to_dict(self):
    return {
      'date': self.date,
      'book': self.book,
      'person': self.person
    }

  def book(self):
    self._book

  def book(self, value):
    self._book = value

  def date(self):
    self._date

  def date(self, value):
    self._date = value

  def person(self):
    self._person

  def person(self, value):
    self._person = value
