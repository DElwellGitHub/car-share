import datetime as dt
import csv

class Car:
    '''
    The Car class is meant to define a car object, which can be owned by owner object,
    and rented by renter object.
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
        
        #Car nickname must be 30 characters or less
        self.__nickname_char_limit = 30
        self.__nickname_assert = f'Nickname must be {self.__nickname_char_limit} characters or less.'
        assert len(nickname)<=self.__nickname_char_limit, self.__nickname_assert
        
        #Car nickname must be unique
        self.__name_used_assert = 'Nickname already used for another car'
        assert nickname not in self.all, self.__name_used_assert
        
        #Car must be 1980 model or later
        self.__oldest_car_year = 1980
        assert int(year)>=self.__oldest_car_year, 'Car is too old.'

        #Car must have a valid year value (i.e. must be next year or less)
        assert int(year)<=int(dt.datetime.now().strftime('%Y'))+1, 'Car year is in the future. Not possible!'

        #Number of miles driven for life of car must be 0 or greater
        assert int(miles_driven_life) >= 0, 'Miles driven cannot be negative.'
        
        #Number of accidents must be 0 or greater
        assert int(accidents_life) >=0, 'Accidents cannot be negative.'

        #City of car must be a valid city (i.e Boston, Philadelphia, New York City)
        assert city in self.__valid_locations[state], 'Sorry, car rental not available in this city/state.'

        #Attributes
        self.__nickname = nickname
        self.__make = make
        self.__model = model
        self.__year = int(year)
        self.__color = color
        self.__miles_driven_life = int(miles_driven_life)
        self.__accidents_life = int(accidents_life)
        self.__city = city
        self.__state = state
        self.__cost_per_hour = float(cost_per_hour)
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
        '''
        Return number of total car instances.
        '''
        return cls.number_of_cars
    @classmethod
    def add_car(cls):
        '''
        Add a car instance.
        '''
        cls.number_of_cars += 1

    @classmethod
    def instantiate_from_csv(cls, file_name):
        '''
        Instantiate a multiple cars from a csv file.
        '''
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
                        cost_per_hour = float(c.get('cost_per_hour'))
                )
            
    
    #Representation of car
    def __repr__(self):
        '''
        Define how we represent car when car instance is called.
        '''
        return f'''Car: {self.nickname}, {self.make}, {self.model}, {self.year}, {self.color}, miles driven: {self.miles_driven_life}, accidents: {self.accidents_life}, location: {self.city}, {self.state}'''
    
    @property
    def nickname(self):
        '''
        Return nickname of car.
        '''
        return self.__nickname
    @nickname.setter
    def nickname(self, value):
        '''
        Change nickname of car.
        '''
        if len(value)> self.__nickname_char_limit:
            raise Exception(self.__nickname_assert)
        elif value in self.all:
            raise Exception(self.__name_used_assert)
        else:
            self.all.remove(self.__nickname)
            self.__nickname = value
            self.all.append(value)
    
    @property
    def make(self):
        '''
        Return make of car.
        '''
        return self.__make
    
    @property
    def model(self):
        '''
        Return model of car.
        '''
        return self.__model
    
    @property
    def year(self):
        '''
        Return year of car.
        '''
        return self.__year

    @property
    def color(self):
        '''
        Return color car.
        '''
        return self.__color
    @color.setter
    def color(self, value):
        '''
        Change color of car.
        '''
        self.__color = value

    @property
    def miles_driven_life(self):
        '''
        Return miles driven for life of car.
        '''
        return self.__miles_driven_life
    @miles_driven_life.setter
    def miles_driven_life(self, value):
        '''
        Change miles driven for life of car.
        '''
        if type(value) is not int or value < 0:
            raise ValueError('Miles incrememnt must be positive number value')
        else:
            self.__miles_driven_life = value
    def increase_miles(self,miles_increment):
        '''
        Change miles driven for life of car by an increment.
        '''
        if (type(miles_increment) is not int 
            and type(miles_increment) is not float) or miles_increment < 0:
            raise ValueError('Miles incrememnt must be positive number value')
        else:
            self.__miles_driven_life += miles_increment 

    @property
    def accidents_life(self):
        '''
        Return number of accidents for life of car.
        '''
        return self.__accidents_life
    @accidents_life.setter
    def accidents_life(self, value):
        '''
        Change number of accidents for life of car.
        '''
        if type(value) is not int or value < 0:
            raise ValueError('Must set number of accidents to integer value of 0 or greater.')
        else:
            self.__accidents_life = value
    def increase_accidents(self,accident_increment=1):
        '''
        Change number of accidents for life of car by an increment.
        '''
        if accident_increment <= 0 or type(accident_increment) is not int:
            raise ValueError('Must choose an integer value of 1 or greater')
        else:
            self.__accidents_life += accident_increment
    
    @property
    def city(self):
        '''
        Return city of car.
        '''
        return self.__city
    @city.setter
    def city(self, value):
        '''
        Change city of car. 
        It must be in one of the valid cities (Boston, Philadelphia, New York City).
        If city is changed, then state is changed too.
        '''
        if value not in self.__valid_locations.values():
            raise Exception('Sorry, car rental not available in this city')
        else:
            self.__city = value
            key_list = list(self.__valid_locations.keys())
            val_list = list(self.__valid_locations.values())
            position = val_list.index(value)
            new_state = key_list[position]
            self.__state = new_state
    
    @property
    def state(self):
        '''
        Return city of car.
        '''
        return self.__state
    @state.setter
    def state(self, value):
        '''
        Change state of car. 
        It must be in one of the valid states(Massachusetts, Pennsylvania, New York).
        If state is changed, then city is changed too.
        '''
        if value not in self.__valid_locations.keys():
            raise Exception('Sorry, car rental not available in this state')
        else:
            self.__state = value
            #If you change state, you must change city too
            self.__city = self.__valid_locations[self.__state]

    @property
    def cost_per_hour(self):
        '''
        Return cost to rent per hour of car.
        '''
        return self.__cost_per_hour
    
    @property
    def owner(self):
        '''
        Return owner of car.
        '''
        return self.__owner
    
