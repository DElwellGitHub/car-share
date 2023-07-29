from carshare_classes.member import Member
import datetime as dt
from dateutil.relativedelta import relativedelta
from carshare_classes.car import Car
import csv

class Owner(Member):
    all = []
    number_of_people = 0
    all_instances = []
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
        self.__list_of_cars = []
        self.__latest_car_added = None

        #Add one to number of unique owners
        if self.__email not in self.all:
            self.add_list_of_all(self.__email)
            self.increment_people_count(cls='Owner')

    @property
    def number_of_cars(self):
        '''
        Return number of cars the owner has registered.
        '''
        return self.__number_of_cars
    @number_of_cars.setter
    def number_of_cars(self,value):
        self.__number_of_cars = value
    
    @property
    def list_of_cars(self):
        '''
        Return list of cars the owner has registered.
        '''
        return self.__list_of_cars
    
    def make_car_available(self, 
                           car_nickname,
                           car_increment=1):
        '''
        Owner adds a car to his list of available cars that people can rent.
        '''
        if car_nickname in Car.all:
            if car_nickname not in self.__list_of_cars:
                self.__number_of_cars += car_increment
                self.__list_of_cars.append(car_nickname)
            else:
                raise Exception('Car is already made available.')
        else:
            raise Exception('Car is not in the system. Please add it first before activiating.')
        

    def make_car_unavailable(self, 
                             car_nickname,
                             car_increment=1):
        '''
        Owner changes a car from available to unavailable to rent.
        '''
        if car_nickname in Car.all:
            if car_nickname in self.__list_of_cars:
                self.__number_of_cars -= car_increment
                self.__list_of_cars.remove(car_nickname)
            else:
                raise Exception('Car is already made unavailable.')
        else:
            raise Exception('Car is not in the system. Please add it first and make it available before trying to remove it..')

    def add_car(self,
                 nickname,
                 make,
                 model,
                 year,
                 color,
                 miles_driven_life,
                 accidents_life,
                 city,
                 state,
                 cost_per_hour):
        '''
        Owner registers a car, which he can then add to list of available cars to rent.
        '''
        self.__latest_car_added = Car(nickname,
                 make,
                 model,
                 year,
                 color,
                 miles_driven_life,
                 accidents_life,
                 city,
                 state,
                 cost_per_hour,
                 owner = self)
        
        self.number_of_cars += 1

    @property
    def latest_car_added(self):
        return self.__latest_car_added
