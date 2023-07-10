from car import Car

class evCar(Car):
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
                 charge:float):
        super().__init__(nickname,
                         make,
                         model,
                         year,
                         color,
                         miles_driven_life,
                         accidents_life,
                         city,
                         state)
        assert float(charge) >=0, "Value must be positive number between 0 and 1."
        assert float(charge) <=1, "Value must be positive number between 0 and 1."
        self.__charge = charge

        @property
        def charge(self):
            return self.__charge
        @charge.setter
        def charge(self,value):
            if self.__charge + value<1:
                return self.__charge + value
            else:
                return 1
