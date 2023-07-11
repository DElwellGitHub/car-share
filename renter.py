from member import Member
import datetime as dt
from dateutil.relativedelta import relativedelta
from car import Car

class Renter(Member):
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
        
        self.__number_of_rentals = 0
        self.__account_balance = 0
        self.__accidents = 0
        self.__current_car = None
        self.__last_car = None

        #Add one to number of unique renters
        if self.__email not in self.all:
            self.add_list_of_all(self.__email)
            self.increment_people_count(cls='Renter')

    #Representation of renter
    def __rep__(self):
        super.__repr__(self,designation='Renter')

    @property
    def number_of_rentals(self):
        return self.__number_of_rentals
        
    @property
    def account_balance(self):
        return self.__account_balance
        
    @property
    def accidents(self):
        return self.__accidents

    def increase_accidents(self,accidents_increment=1):
        self.__accidents += accidents_increment

    def update_account_balance(self, change):
        self.__account_balance += change

    def increase_rental_count(self,rental_increment=1):
        self.__number_of_rentals += 1

    @property
    def current_car(self):
        return self.__current_car
    
    def rentCar(self,car_rented):
        self.increase_rental_count()
        self.__current_car = car_rented

    @property
    def last_car(self):
        return self.__last_car

    def returnCar(self,
                  miles_driven,
                  accidents):
        if accidents > 0:
            self.increase_accidents(accidents)
            self.update_account_balance(2000)
        self.__last_car = self.__current_car
        self.__current_car = None

        

        