import datetime as dt
class Car:
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
        
        #Assertions
        assert len(nickname)<=14, 'Nickname must be 14 characters or less.'
        assert int(year)>1980, 'Car is too old.'
        assert int(year)<=int(dt.datetime.now().strftime('%Y'))+1, 'Car year is incorrect'
        assert int(miles_driven_life) >= 0, 'Miles driven cannot be negative.'
        assert int(accidents_life) >=0, 'Accidents cannot be negative.'
        

        #Attributes
        self.nickname = nickname
        self.make = make
        self.model = model
        self.year = int(year)
        self.color = color
        self.miles_driven_life = int(miles_driven_life)
        self.accidents_life = accidents_life
        self.city = city
        self.state = state

        #Nickname
        @property
        def nickname(self):
            return self.nickname
        @nickname.setter
        def nickname(self, value):
            self.nickname = value
        
        #Make
        @property
        def make(self):
            return self.make
        
        #Model
        @property
        def model(self):
            return self.model
        
        #Year
        @property
        def year(self):
            return self.year

        #Color
        @property
        def color(self):
            return self.color
        @color.setter
        def color(self, value):
            self.color = value

        #Miles Driven Life
        @property
        def miles_driven_life(self):
            return self.miles_driven_life
        @miles_driven_life.setter
        def miles_driven_life(self, value):
            self.miles_driven_life = value

        #Accidents Life
        @property
        def accidents_life(self):
            return self.accidents_life
        @accidents_life.setter
        def accidents_life(self, value):
            return self.accidents_life
        
        #City
        @property
        def city(self):
            return self.city
        @city.setter
        def city(self, value):
            return self.city
        
        #State
        @property
        def state(self):
            return self.state
        @state.setter
        def state(self, value):
            return self.state
        

