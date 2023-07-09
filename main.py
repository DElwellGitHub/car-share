from car import Car
from ev_car import evCar
import datetime as dt
from dateutil.relativedelta import relativedelta
from member import Member

def main():
    kwargs = {'nickname':'Mysty',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania'}
    car1 = Car(**kwargs)

    kwargs = {'nickname':'Mysty2',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania'}
    car1 = Car(**kwargs)

    print(car1.nickname)
    print(car1.miles_driven_life)
    #print(car1.city)
    #print(car1.state)
    #print(car1.city)
    #car1.all
    #print(car1.city)
    car1.state='New York'
    print(car1.city)
    #car1.increase_accidents(-1)
    print(car1.accidents_life)
    print(car1.all)
    print(Car.all)
    print(car1)
    print(Car.number_of_cars)



    kwargs = {'nickname':'evcar',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania',
              'charge':1}
    
    ev_car_1 = evCar(**kwargs)
    print(ev_car_1)
    ev_car_1.charge = .5
    print(dt.date.today())
    print(dt.date.today() - relativedelta(years=18))
    test_year = dt.date.today() - relativedelta(years=18)
    test_year_2 = dt.date(year=2008, month=12,day=1)
    print(test_year_2 < test_year)


    kwargs = {'first_name':'John',
              'last_name':'Smith',
              'date_of_birth': dt.date(year=2008, month=1, day=1),
              'email':'john.smith@gmail.com'}
    
    member_1 = Member(**kwargs)

    print(member_1.all)
if __name__=='__main__':
    main()