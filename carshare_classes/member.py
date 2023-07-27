import datetime as dt
from dateutil.relativedelta import relativedelta
import re
import csv

class Member:
    all = []
    number_of_people = 0
    all_instances = []
    def __init__(self,
                 first_name,
                 last_name,
                 date_of_birth:dt.date,
                 email):

        assert len(first_name) < 20, 'First name must be less than 20 characters.'
        assert len(last_name) < 20, 'Last name must be less than 20 characters.'
        assert date_of_birth < dt.date.today() - relativedelta(years=18), 'Must be 18 or older to sign up!'
        
        regex_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        assert re.fullmatch(regex_pattern, email), "Invalid email."

        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        self.__sign_up_date = dt.datetime.now()
        self.__number_of_rentals = 0
        self.__account_balance = 0


        #Add one to number of unique members
        if self.__email not in self.all:
            self.add_list_of_all(self.__email)
            self.increment_people_count()
            self.add_all_instances(self)

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def increment_people_count(cls='Member'):
        cls.number_of_people += 1
    
    @classmethod
    def add_list_of_all(cls,email):
        cls.all.append(email)
    
    @classmethod
    def add_all_instances(cls,self):
        cls.all_instances.append(self)

    #Representation of member
    def __repr__(self):
        '''
        Define how we represent member when it is called.
        '''
        return f'{self.__class__.__name__}: {self.first_name} {self.last_name}, {self.email}'
    
    #First Name
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    #Last Name
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
    
    #Date of Birth
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    #Email
    @property
    def email(self):
        return self.__email

    #Sign up date
    @property
    def sign_up_date(self):
        return self.__sign_up_date
    
    @property
    def number_of_rentals(self):
        return self.__number_of_rentals
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    def increase_rental_count(self,rental_increment=1):
        '''
        Increase the number of rentals attributed to member.
        '''
        self.__number_of_rentals += rental_increment

    def update_account_balance(self, change):
        '''
        Update member's account balance.
        '''
        self.__account_balance += change
