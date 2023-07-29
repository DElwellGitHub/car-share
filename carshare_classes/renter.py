from carshare_classes.member import Member
import datetime as dt
from dateutil.relativedelta import relativedelta
from carshare_classes.car import Car

class Renter(Member):
    '''
    Renter class is a child class of Member.
    A renter will rent an owner's car.
    '''
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
        
        #Attributes
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        
        self.__accidents = 0
        self.__current_car = None
        self.__last_car = None
        self.__datetime_start = None
        self.__datetime_return = None

        #Add one to number of unique renters
        if self.__email not in self.all:
            self.add_list_of_all(self.__email)
            self.increment_people_count(cls='Renter')
        
    @property
    def accidents(self):
        '''
        Return number of accidents that the renter has had.
        '''
        return self.__accidents

    def increase_accidents(self,accidents_increment=1):
        '''
        Increase number of accidents attributed to renter.
        '''
        self.__accidents += accidents_increment

    @property
    def current_car(self):
        '''
        Return current car that the renter has taken out.
        '''
        return self.__current_car
    
    @property
    def last_car(self):
        '''
        Return the last car that the renter has taken out and returned.
        '''
        return self.__last_car
    
    @property
    def datetime_start(self):
        '''
        Return the date and time at which the renter will take out the car.
        '''
        return self.__datetime_start
    @datetime_start.setter
    def datetime_start(self,value):
        '''
        Set the date and time at which the renter will take out the car.
        '''
        self.__datetime_start = value

    @property
    def datetime_return(self):
        '''
        Return the date and time at which the renter will return the car.
        '''
        return self.__datetime_return
    @datetime_return.setter
    def datetime_return(self,value):
        '''
        Set the date and time at which the renter will take out the car.
        '''
        self.__datetime_return = value
    
    def rent_car(self,
                car_rented,
                datetime_start,
                datetime_return):
        '''
        Renter rents a car.
        '''
        if datetime_start > datetime_return:
            raise ValueError('Start date and time must be before return date and time.')
        else:
            self.increase_rental_count()
            self.__current_car = car_rented
            self.__datetime_start = datetime_start
            self.__datetime_return = datetime_return

    def return_car(self,
                  miles_driven,
                  accidents,
                  real_time_return = True):
        '''
        Renter returns the car they had rented
        '''
        if accidents > 0:
            #Increase renter's count of accidents
            self.increase_accidents(accidents)
            #Increase renter's account balance by 2000 (penalty for accident)
            self.update_account_balance(-2000*accidents)
            #Increase car's count of accidents
            self.__current_car.increase_accidents(accident_increment=accidents)
        
        #Check to make sure that renter returns car on time
        if real_time_return and dt.datetime.now() > self.__datetime_return:
            #Apply a 50 dollar penalty
            self.update_account_balance(-50)
            #Set return time as now
            self.__datetime_return = dt.datetime.now()

        #Incrase renter's account balance by hours * cost per hour
        time_elapsed = self.__datetime_return - self.__datetime_start
        hours_elapsed = float(time_elapsed.total_seconds()) / 3600
        self.update_account_balance(-1*hours_elapsed*self.__current_car.cost_per_hour)

        #Increase owner of car's account balance
        if self.__current_car.owner:
            self.__current_car.owner.update_account_balance(1*hours_elapsed*self.__current_car.cost_per_hour)
        
        #Increase car's miles driven for life
        self.__current_car.increase_miles(miles_increment = miles_driven)

        #Make last car be the current car
        self.__last_car = self.__current_car

        #Remove current car
        self.__current_car = None
        

        

        