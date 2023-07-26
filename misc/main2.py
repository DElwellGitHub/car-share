from car import Car
from ev_car import evCar
import datetime as dt
from dateutil.relativedelta import relativedelta
from member import Member
from renter import Renter
from owner import Owner

def main():
    kwargs1 = {'nickname':'Mysty',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania',
              'cost_per_hour':14.5}
    car1 = Car(**kwargs1)

    kwargs = {'first_name':'Bob',
              'last_name':'Dylan',
              'date_of_birth':dt.date(year=2002, month=1, day=1),
              'email':'bob.dylan@gmail.com'}

    owner_1 = Owner(**kwargs)

    kwargs3 = {'nickname':'Mysty333',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania',
              'cost_per_hour':14.5}

    print(owner_1)

    owner_1.add_car(**kwargs3)
    print(owner_1.latest_car_added)

if __name__=='__main__':
    main()