import datetime as dt
class Car:
    '''
    The Car class will be the parent class for all vehicles (EV class or GasCar class) that can be rented.
    '''
    def __init__(self, 
                 nickname:str,
                 make:str,
                 model:str,
                 year,
                 color:str,
                 miles_driven_life,
                 accidents_life,
                 city:str,
                 state:str):
        
        #Valid locations {state:city}
        self.__valid_locations = {'Pennsylvania':'Philadelphia',
                           'New York':'New York',
                           'Massachusetts':'Boston'}

        #Assertions
        assert len(nickname)<=14, 'Nickname must be 14 characters or less.'
        assert int(year)>1980, 'Car is too old.'
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

    #Nickname
    @property
    def nickname(self):
        return self.__nickname
    @nickname.setter
    def nickname(self, value):
        self.__nickname = value
    
    #Make
    @property
    def make(self):
        return self.__make
    
    #Model
    @property
    def model(self):
        return self.__model
    
    #Year
    @property
    def year(self):
        return self.__year

    #Color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, value):
        self.__color = value

    #Miles Driven Life
    @property
    def miles_driven_life(self):
        return self.__miles_driven_life
    @miles_driven_life.setter
    def miles_driven_life(self, value):
        self.__miles_driven_life = value

    #Accidents Life
    @property
    def accidents_life(self):
        return self.__accidents_life
    @accidents_life.setter
    def accidents_life(self, value):
        return self.__accidents_life
    
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
            #Change state too
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
        return self.__state
    

