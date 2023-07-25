import unittest
from renter import Renter
import datetime as dt
from dateutil.relativedelta import relativedelta
from car import Car

class TestRenter(unittest.TestCase):

    def setUp(self):
        Renter.all = []
        Renter.number_of_people = 0

        self.renter_1_kwargs = {'first_name':'Brett',
                                'last_name':'Gardner', 
                                'date_of_birth':dt.date(year=1983,month=8,day=24),
                                'email':'brett.gardner@nyy.com'}
        self.renter_1 = Renter(**self.renter_1_kwargs)
        

        self.renter_2_kwargs = {'first_name':'Bob',
                                'last_name':'Dylan',
                                'date_of_birth': dt.date(year=2002, month=1, day=1),
                                'email':'bob.dylan@gmail.com'}
        self.renter_2 = Renter(**self.renter_2_kwargs)
        
        Car.all = []
        Car.number_of_cars = 0
        
        self.car_1_kwargs = {'nickname':'Mystery Machine',
                      'make':'volkswagen',
                      'model':'vw bus',
                      'year':'1999',
                      'color':'tie dye',
                      'miles_driven_life':200000,
                      'accidents_life':1,
                      'city':'Philadelphia',
                      'state':'Pennsylvania',
                      'cost_per_hour':14.5}
        self.car_1 = Car(**self.car_1_kwargs)
        
        self.car_2_kwargs = {'nickname':'Speed Racer',
                      'make':'Toyota',
                      'model':'Prius',
                      'year':'2012',
                      'color':'red',
                      'miles_driven_life':150000,
                      'accidents_life':2,
                      'city':'Boston',
                      'state':'Massachusetts',
                      'cost_per_hour':11.5}
        self.car_2 = Car(**self.car_2_kwargs)

    def tearDown(self):
        pass

    #Todo - determine what to test and create tests
    def test_rent_return_car(self):
        '''
        Test renting and returning acar.
        '''
        self.assertNotEqual(self.renter_1.current_car,self.car_1)
        start_time = dt.datetime(year=2023,month=7,day=1,hour=12,minute=30)
        return_time = dt.datetime(year=2023,month=7,day=1,hour=15,minute=30)
        self.renter_1.rentCar(self.car_1,
                              start_time,
                              return_time)
        self.assertEqual(self.renter_1.current_car,self.car_1)
        self.assertEqual(self.renter_1.datetime_start,start_time)
        self.assertEqual(self.renter_1.datetime_return,return_time)
        self.assertNotEqual(self.renter_2.current_car,self.car_1)
        
        self.renter_1.returnCar(miles_driven=100,
                                 accidents=0,
                                real_time_return=False)
        predicted_cost = -14.5*3
        self.assertEqual(self.renter_1.account_balance,predicted_cost)

        start_time = dt.datetime(year=2023,month=7,day=1,hour=12,minute=30)
        return_time = dt.datetime(year=2023,month=6,day=30,hour=15,minute=30)

        #Test with a start time after return time.
        with self.assertRaises(ValueError):
            start_time = dt.datetime(year=2023,month=7,day=1,hour=12,minute=30)
            return_time = dt.datetime(year=2023,month=6,day=30,hour=15,minute=30)
            self.renter_2.rentCar(self.car_2,
                                start_time,
                                return_time)

        start_time = dt.datetime(year=2023,month=7,day=1,hour=12,minute=30)
        return_time = dt.datetime(year=2023,month=7,day=1,hour=18,minute=0)
        self.renter_2.rentCar(self.car_2,
                              start_time,
                              return_time)
        self.renter_2.returnCar(miles_driven=200,
                                accidents=1,
                                real_time_return=False)
        predicted_cost = -11.5*5.5-2000
        self.assertEqual(self.renter_2.account_balance,predicted_cost)

    def test_pay_account(self):
        '''
        Test paying account balance.
        '''
        start_time = dt.datetime(year=2023,month=7,day=1,hour=12,minute=30)
        return_time = dt.datetime(year=2023,month=7,day=1,hour=18,minute=0)

        self.renter_1.rentCar(self.car_1,
                              start_time,
                              return_time)
        
        self.renter_1.returnCar(miles_driven=200,
                                accidents=1,
                                real_time_return=False)
        predicted_cost = -14.5*5.5-2000
        self.assertEqual(self.renter_1.account_balance,predicted_cost)
        
        one_third_payment = predicted_cost/-3
        self.renter_1.update_account_balance(one_third_payment)
        self.assertEqual(self.renter_1.account_balance,one_third_payment*-2)

        self.renter_1.update_account_balance(one_third_payment)
        self.assertEqual(self.renter_1.account_balance,one_third_payment*-1)

        self.renter_1.update_account_balance(one_third_payment)
        self.assertEqual(self.renter_1.account_balance,0)

    def test_attributes(self):
        '''
        Test changing attributes of renter.
        '''
        self.assertEqual(self.renter_1.email,'brett.gardner@nyy.com')
        self.assertEqual(Renter.number_of_people,2 )

        self.assertEqual(self.renter_1.first_name,'Brett')
        self.assertEqual(self.renter_1.last_name,'Gardner')

if __name__ == '__main__':
    unittest.main()



