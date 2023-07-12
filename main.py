from car import Car
from ev_car import evCar
import datetime as dt
from dateutil.relativedelta import relativedelta
from member import Member
from renter import Renter
from owner import Owner

def main():
    kwargs = {'nickname':'Mysty',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania',
              'cost_per_hour':14.5}
    car1 = Car(**kwargs)

    kwargs = {'nickname':'Mysty2',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania',
              'cost_per_hour':13.75}
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
              'charge':1,
              'cost_per_hour':12.75}
    
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
              'date_of_birth': dt.date(year=2002, month=1, day=1),
              'email':'john.smith@gmail.com'}
    
    member_1 = Member(**kwargs)

    kwargs = {'first_name':'Jane',
              'last_name':'Doe',
              'date_of_birth': dt.date(year=2002, month=1, day=1),
              'email':'jane.doe@gmail.com'}

    renter_1 = Renter(**kwargs)

    kwargs = {'first_name':'Bob',
              'last_name':'Dylan',
              'date_of_birth': dt.date(year=2002, month=1, day=1),
              'email':'bob.dylan@gmail.com'}

    renter_2 = Renter(**kwargs)

    print(member_1.all)
    print(renter_1.all)
    print(Renter.all)
    print(Renter.number_of_people)
    print(Member.number_of_people)
    print(car1)
    renter_1.rentCar(car1)
    print(renter_1.current_car)
    print(type(renter_1))
    renter_1.returnCar(miles_driven=100,accidents=1,hours=7)
    print(renter_1.current_car)
    print(renter_1.last_car)
    print(renter_1.sign_up_date)
    print(renter_1.number_of_rentals)
    renter_1.accidents

    print(car1.accidents_life)
    print(car1.miles_driven_life)
    print(renter_1.account_balance)
    print(renter_1.first_name)


    kwargs = {'first_name':'Bob',
              'last_name':'Dylan',
              'date_of_birth': dt.date(year=2002, month=1, day=1),
              'email':'bob.owner@gmail.com'}

    owner_1 = Owner(**kwargs)

    print(owner_1)
    print(renter_1)
if __name__=='__main__':
    main()