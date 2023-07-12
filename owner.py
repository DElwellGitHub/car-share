from member import Member
import datetime as dt
from dateutil.relativedelta import relativedelta
from car import Car

class Owner(Member):
    all = []
    number_of_people = 0
    def __init__(self,
                 first_name,
                 last_name,
                 date_of_birth:dt.date,
                 email):
        super().__init__(first_name,
                         last_name,
                         date_of_birth,
                         email)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email

        self.__number_of_cars = 0

        #Add one to number of unique owners
        if self.__email not in self.all:
            self.add_list_of_all(self.__email)
            self.increment_people_count(cls='Owner')

    @property
    def number_of_cars(self):
        return self.__number_of_cars
    
    def add_car(self, number_of_cars=1):
        self.__number_of_cars += number_of_cars

    def remove_cars(self, number_of_cars=1):
        self.__number_of_cars -= number_of_cars


