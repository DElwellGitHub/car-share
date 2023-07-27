import datetime as dt
import csv

class Car:
    '''
    The Car class will be the parent class for all vehicles (EV class or GasCar class) that can be rented.
    '''
    all = []
    all_instances = []
    number_of_cars = 0
    def __init__(self, 
                 nickname:str,
                 make:str,
                 model:str,
                 year,
                 color:str,
                 miles_driven_life,
                 accidents_life,
                 city:str,
                 state:str,
                 cost_per_hour:float,
                 owner = None):
        
        #Valid locations {state:city}
        self.__valid_locations = {'Pennsylvania':'Philadelphia',
                           'New York':'New York City',
                           'Massachusetts':'Boston'}
        
        #Nickname character limit
        self.__nickname_char_limit = 30
        self.__nickname_assert = f'Nickname must be {self.__nickname_char_limit} characters or less.'
        self.__name_used_assert = 'Nickname already used for another car'

        #Oldest car year accepted
        self.__oldest_car_year = 1980

        #Assertions
        assert len(nickname)<=self.__nickname_char_limit, self.__nickname_assert
        assert nickname not in self.all, self.__name_used_assert
        assert int(year)>=self.__oldest_car_year, 'Car is too old.'
        assert int(year)<=int(dt.datetime.now().strftime('%Y'))+1, 'Car year is in the future. Not possible!'
        assert int(miles_driven_life) >= 0, 'Miles driven cannot be negative.'
        assert int(accidents_life) >=0, 'Accidents cannot be negative.'
        assert city in self.__valid_locations[state], 'Sorry, car rental not available in this city/state.'

        #Attributes
        self.__nickname = nickname
        self.__make = make
        self.__model = model
        self.__year = int(year)
        self.__color = color
        self.__miles_driven_life = int(miles_driven_life)
        self.__accidents_life = accidents_life
        self.__city = city
        self.__state = state
        self.__cost_per_hour = cost_per_hour
        self.__owner = owner

        #Add one to number of unique nicknames of cars
        if self.__nickname not in self.all:
            self.add_car()

        #Add nickname to list of all
        self.all.append(self.__nickname)

        #Add instance to list of all instances
        self.all_instances.append(self)

    @classmethod
    def number_of_cars_(cls):
        return cls.number_of_cars
    @classmethod
    def add_car(cls):
        cls.number_of_cars += 1

    @classmethod
    def instantiate_from_csv(cls, file_name):
        with open(file_name, 'r') as f:
            csvreader = csv.DictReader(f)
            cars = list(csvreader) 
            for c in cars:
                Car(
                        nickname = c.get('nickname'),
                        make = c.get('make'),
                        model = c.get('model'),
                        year = c.get('year'),
                        color = c.get('color'),
                        miles_driven_life = int(c.get('miles_driven_life')),
                        accidents_life = int(c.get('accidents_life')),
                        city = c.get('city'),
                        state = c.get('state'),
                        cost_per_hour = c.get('cost_per_hour')
                )
            
    
    #Representation of car
    def __repr__(self):
        '''
        Define how we represent car when it is called.
        '''
        return f'''Car: {self.nickname}, {self.make}, {self.model}, {self.year}, {self.color}, miles driven: {self.miles_driven_life}, accidents: {self.accidents_life}, location: {self.city}, {self.state}'''
    
    #Nickname of car
    @property
    def nickname(self):
        return self.__nickname
    @nickname.setter
    def nickname(self, value):
        if len(value)> self.__nickname_char_limit:
            raise Exception(self.__nickname_assert)
        elif value in self.all:
            raise Exception(self.__name_used_assert)
        else:
            self.all.remove(self.__nickname)
            self.__nickname = value
            self.all.append(value)
    
    #Make of car
    @property
    def make(self):
        return self.__make
    
    #Model of car
    @property
    def model(self):
        return self.__model
    
    #Year of car
    @property
    def year(self):
        return self.__year

    #Color of car
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value

    #Miles Driven Life of car
    @property
    def miles_driven_life(self):
        return self.__miles_driven_life
    @miles_driven_life.setter
    def miles_driven_life(self, value):
        if type(value) is not int or value < 0:
            raise ValueError('Miles incrememnt must be positive number value')
        else:
            self.__miles_driven_life = value
    def increase_miles(self,miles_increment):
        if (type(miles_increment) is not int 
            and type(miles_increment) is not float) or miles_increment < 0:
            raise ValueError('Miles incrememnt must be positive number value')
        else:
            self.__miles_driven_life += miles_increment 

    #Accidents Life of car
    @property
    def accidents_life(self):
        return self.__accidents_life
    @accidents_life.setter
    def accidents_life(self, value):
        if type(value) is not int or value < 0:
            raise ValueError('Must set number of accidents to integer value of 0 or greater.')
        else:
            self.__accidents_life = value
    def increase_accidents(self,accident_increment=1):
        '''
        Record an increase of the number of accidents.
        '''
        if accident_increment <= 0 or type(accident_increment) is not int:
            raise ValueError('Must choose an integer value of 1 or greater')
        else:
            self.__accidents_life += accident_increment
    
    #City
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, value):
        if value not in self.__valid_locations.values():
            raise Exception('Sorry, car rental not available in this city')
        else:
            self.__city = value
            #If you change city, you must change state too
            key_list = list(self.__valid_locations.keys())
            val_list = list(self.__valid_locations.values())
            position = val_list.index(value)
            new_state = key_list[position]
            self.__state = new_state
    
    #State
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, value):
        if value not in self.__valid_locations.keys():
            raise Exception('Sorry, car rental not available in this state')
        else:
            self.__state = value
            #If you change state, you must change city too
            self.__city = self.__valid_locations[self.__state]

    #Cost per hour
    @property
    def cost_per_hour(self):
        return self.__cost_per_hour
    
    #Owner of car
    @property
    def owner(self):
        return self.__owner
    

