class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle, capacity):
        super().__init__(name_of_vehicle, max_speed, average_of_vehicle)
        self.capacity = capacity

    def seating_capacity(self):
        print(self.name_of_vehicle, self.capacity)

myFirstCar = Car('ALTO', 200, '$5600', 4)
myFirstCar.seating_capacity()

##################################################################################################################
# Multiple inheritance is a child class inheriting attributes and methods from multiple parent classes. 

class Book:
    def __init__(self, name_of_book, publishing_year):
        self.name_of_book = name_of_book
        self.publishing_year = publishing_year

class Author:
    def __init__(self, name_of_author, death_year, best_selling_book):
        self.name_of_author = name_of_author
        self.death_year = death_year
        self.best_selling_book = best_selling_book

# Library inherits from multiple classes
class Library(Book, Author):
    def __init__(self, name_of_book, publishing_year, name_of_author, death_year, best_selling_book):
        Book.__init__(self, name_of_book, publishing_year)
        Author.__init__(self, name_of_author, death_year, best_selling_book)

    def book_author(self):
        print(f"{self.name_of_book} is written by {self.name_of_author}")

library_book = Library('Jane Eyre', 1890, 'Jane Austen', 1900, 'Jane Eyre')
library_book.book_author()

#########################################################################################################
class Person:
  # Constructor to initiaize properties
  def __init__(self, name, age, gender):
    self.name = name
    self.__age = age # Encapsulate the age property
    self.gender = gender

  def say_hello(self):
    print(f"Hello, I am {self.name}.")

  def is_adult(self):
    if self.age >= 18:
      return True
    else:
      return False
  
  # Access the age property
  def get_age(self):
    return self.__age

  # Change the age property
  def set_age(self, age):
     self.__age = age
