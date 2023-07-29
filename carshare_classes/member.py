import datetime as dt
from dateutil.relativedelta import relativedelta
import re
import csv

class Member:
    '''
    Member class is the parent class of Owner and Renter.
    An owner will own a car and rent it out to a renter.
    '''
    all = []
    number_of_people = 0
    all_instances = []
    def __init__(self,
                 first_name,
                 last_name,
                 date_of_birth:dt.date,
                 email):
        
        #Name character limits
        assert len(first_name) < 20, 'First name must be less than 20 characters.'
        assert len(last_name) < 20, 'Last name must be less than 20 characters.'
        
        #Must be at least 18 years old to be a member.
        assert date_of_birth < dt.date.today() - relativedelta(years=18), 'Must be 18 or older to sign up!'
        
        #Email must follow a valid email pattern (e.g. john.doe@gmail.com)
        regex_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        assert re.fullmatch(regex_pattern, email), "Invalid email."

        #Attributes
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
        '''
        Return number of members.
        '''
        return cls.number_of_people
    
    @classmethod
    def increment_people_count(cls='Member'):
        '''
        Incremment number of members by one.
        '''
        cls.number_of_people += 1
    
    @classmethod
    def add_list_of_all(cls,email):
        '''
        Add member's email (i.e. their unique identifier) to list of all members.
        '''
        cls.all.append(email)
    
    @classmethod
    def add_all_instances(cls,self):
        '''
        Add member to a list of all members.
        '''
        cls.all_instances.append(self)

    @classmethod
    def instantiate_from_csv(cls, file_name):
        '''
        Insantiate multiple members from a csv file.
        '''
        with open(file_name, 'r') as f:
            csvreader = csv.DictReader(f)
            members = list(csvreader) 
            for m in members:
                cls(
                        first_name = m.get('first_name'),
                        last_name = m.get('last_name'),
                        date_of_birth = dt.date(year = int(m.get('year_birth')),
                                                month = int(m.get('month_birth')),
                                                day = int(m.get('day_birth'))
                                                ),
                        email = m.get('email')
                )

    def __repr__(self):
        '''
        Define how we represent member when it is called.
        '''
        return f'{self.__class__.__name__}: {self.first_name} {self.last_name}, {self.email}'
    
    @property
    def first_name(self):
        '''
        Return first name of member.
        '''
        return self.__first_name
    @first_name.setter
    def first_name(self, value):
        '''
        Change first name of member.
        '''
        self.__first_name = value

    #Last Name
    @property
    def last_name(self):
        '''
        Return last name of member.
        '''
        return self.__last_name
    @last_name.setter
    def last_name(self, value):
        '''
        Change last name of member.
        '''
        self.__last_name = value
    
    @property
    def date_of_birth(self):
        '''
        Return member's date of birth.
        '''
        return self.__date_of_birth

    @property
    def email(self):
        '''
        Return member's email.
        '''
        return self.__email

    @property
    def sign_up_date(self):
        '''
        Return member's sign up date.
        '''
        return self.__sign_up_date
    
    @property
    def number_of_rentals(self):
        '''
        Return the number of rentals that the member has had.
        '''
        return self.__number_of_rentals
    
    @property
    def account_balance(self):
        '''
        Return account balance of member.
        '''
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
