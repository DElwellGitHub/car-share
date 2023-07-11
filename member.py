import datetime as dt
from dateutil.relativedelta import relativedelta

class Member:
    all = []
    number_of_people = 0
    def __init__(self,
                 first_name,
                 last_name,
                 date_of_birth:dt.date,
                 email):

        assert len(first_name) < 20, 'First name must be less than 20 characters.'
        assert len(last_name) < 20, 'Last name must be less than 20 characters.'
        assert date_of_birth < dt.date.today() - relativedelta(years=18), 'Must be 18 or older to sign up!'

        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__email = email
        self.__sign_up_date = dt.datetime.now()


        #Add one to number of unique members
        if self.__email not in self.all:
            self.add_list_of_all(self.__email)
            self.increment_people_count()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def increment_people_count(cls='Member'):
        cls.number_of_people += 1
    
    @classmethod
    def add_list_of_all(cls,email):
        cls.all.append(email)

    #Representation of member
    def __repr__(self,designation='Member'):
        '''
        Define how we represent car when it is called.
        '''
        return f'{designation}: {self.first_name} {self.last_name}, {self.email}'
    
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
