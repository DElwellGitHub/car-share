import datetime as dt

class member:
    all = []
    number_of_members = 0
    def __init__(self,
                 first_name,
                 last_name,
                 city,
                 state,
                 date_of_birth,
                 gender,
                 email,
                 phone_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__email = email
        self.__sign_up_date = dt.datetime.now()


        #Add one to number of unique nicknames of cars
        if self.__email not in self.all:
            self.add_member()

        #Add email to list of all
        self.all.append(self.__email)

    @classmethod
    def number_of_members_(cls):
        return cls.number_of_members
    
    @classmethod
    def add_member(cls):
        cls.number_of_members += 1

    #Representation of member
    def __repr__(self):
        '''
        Define how we represent car when it is called.
        '''
        return f'Member: {self.first_name} {self.last_name}, {self.email}'
    
    #First Name
    @property
    def first_name(self):
        return self.__first_name

    #Last Name
    @property
    def first_name(self):
        return self.__last_name
    
    #Date of Birth
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    #Gender
    @property
    def gender(self):
        return self.__gender

    #Email
    @property
    def email(self):
        return self.__email

    #Sign up date
    @property
    def sign_up_date(self):
        return self.__sign_up_date
