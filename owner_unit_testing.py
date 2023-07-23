import unittest
import datetime as dt
from owner import Owner
from car import Car

class TestOwner(unittest.TestCase):
    def setUp(self):
        Owner.all = []
        Owner.number_of_people = 0

        self.owner_1 = Owner('John',
                             'Smith',
                             dt.date(year=1985, month=4, day=2),
                             'john.smith@gmail.com')
        
        self.owner_2 = Owner('Jane',
                             'Doe',
                             dt.date(year=1982,
                                     month=5,
                                     day=22),
                            'jane.doe@gmail.com')
        
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

        
    def tearDown(self):
        pass

    def test_first_name(self):
        '''
        Test changing an owner's first name.
        '''
        orig_first_name = self.owner_1.first_name
        new_first_name = 'David'
        self.owner_1.first_name = new_first_name
        self.assertEqual(self.owner_1.first_name, new_first_name)
        self.assertNotEqual(self.owner_1.first_name,orig_first_name)

    def test_last_name(self):
        '''
        Test changing an owner's last name.
        '''
        orig_last_name = self.owner_1.last_name
        new_last_name = 'Robinson'
        self.owner_1.last_name = new_last_name
        self.assertEqual(self.owner_1.last_name, new_last_name)
        self.assertNotEqual(self.owner_1.last_name,orig_last_name)

    def test_immutable_attributes(self):
        '''
        Test trying to change immutable attributes for an owner 
        (i.e. email, sign up date, date of birth, etc.).
        '''
        with self.assertRaises(AttributeError):
            self.owner_2.email = 'jane.fonda@yahoo.com'

        with self.assertRaises(AttributeError):
            self.owner_2.sign_up_date = dt.date(year=2023,month=7,day=4)

        with self.assertRaises(AttributeError):
            self.owner_2.date_of_birth = dt.date(year=1988,month=7,day=20)
        
    def test_too_young(self):
        '''
        Test trying to create an owner that is too young.
        '''
        with self.assertRaises(AssertionError):
            self.young_owner = Owner('John',
                                     'Smith',
                                      dt.date(year=2019, month=4, day=2),
                                     'john.smith@gmail.com')
    def test_invalid_email(self):
        '''
        Test trying to create an owner with an invalid email pattern.
        '''
        bad_emails = ['joeemail.com',
                      'joeemail@gmail.',
                      '@gmail.com',
                      'e@.com',
                      'e@.com.org',
                      'john@gmail.com.']
        
        for email in bad_emails:
            with self.assertRaises(AssertionError):
                self.bad_email_owner = Owner('Joe',
                                             'Johnson',
                                              dt.date(year=1980,month=9,day=22),
                                              email)
    def test_add_car(self):
        '''
        Test adding a car to owner's list of registered cars.
        '''
        
        self.owner_1.add_car(**self.car_1_kwargs)
        self.assertEqual(self.owner_1.latest_car_added.nickname,'Mystery Machine')

        self.owner_1.add_car(**self.car_2_kwargs)
        self.assertEqual(self.owner_1.latest_car_added.nickname,'Speed Racer')
        self.assertNotEqual(self.owner_1.latest_car_added.nickname,'Mystery Machine')


    def test_ineligible_car(self):
        '''
        Test adding an ineligible car to owner's list of registerd cars
        '''

        #Add car from ineligible city
        self.bad_city_kwargs = self.car_1_kwargs
        self.bad_city_kwargs['city'] = 'Miami'
        with self.assertRaises(AssertionError):
            self.owner_1.add_car(**self.bad_city_kwargs)

        #Add car from ineligible state
        self.bad_city_kwargs = self.car_1_kwargs
        self.bad_city_kwargs['state'] = 'Florida'
        with self.assertRaises(KeyError):
            self.owner_1.add_car(**self.bad_city_kwargs)

    def test_make_car_available(self):
        '''
        Test making a registered car available.
        '''
        self.owner_1.add_car(**self.car_1_kwargs)
        self.owner_1.make_car_available('Mystery Machine')
        self.assertIn('Mystery Machine',self.owner_1.list_of_cars)
        self.assertNotIn('Speed Racer',self.owner_1.list_of_cars)

        #Try making a car not registered as available
        with self.assertRaises(Exception):
            self.owner_1.make_car_available('Night Rider')

        #Try making a car that is already active be activated again
        with self.assertRaises(Exception):
            self.owner_1.make_car_available('Mystery Machine')

    def test_make_car_unavailable(self):
        '''
        Test making an available car unavailable.
        '''
        self.owner_1.add_car(**self.car_1_kwargs)
        self.owner_1.make_car_available('Mystery Machine')

        self.owner_1.make_car_unavailable('Mystery Machine')
        self.assertNotIn('Mystery Machine',self.owner_1.list_of_cars)

        #Try making a car not regstered as unavailable
        with self.assertRaises(Exception):
            self.owner_1.make_car_unavailable('Night Rider')

        #Try making a car that is already unactivate be unactivated again
        with self.assertRaises(Exception):
            self.owner_1.make_car_unavailable('Mystery Machine')

    def test_number_of_cars(self):
        '''
        Test that number of cars attribute works.
        '''
        self.assertEqual(0,self.owner_1.number_of_cars)
        self.owner_1.add_car(**self.car_1_kwargs)
        self.assertEqual(1,self.owner_1.number_of_cars)
        self.owner_1.add_car(**self.car_2_kwargs)
        self.assertEqual(2, self.owner_1.number_of_cars)

        self.assertNotEqual(2, self.owner_2.number_of_cars)

    def test_list_of_cars(self):
        '''
        Test that list of cars attribute works.
        '''
        self.assertEqual([],self.owner_1.list_of_cars)
        self.owner_1.add_car(**self.car_1_kwargs)
        self.owner_1.make_car_available('Mystery Machine')
        self.assertEqual(['Mystery Machine'],self.owner_1.list_of_cars)
        self.assertNotEqual(['Mystery Machine'],self.owner_2.list_of_cars)
        self.owner_1.add_car(**self.car_2_kwargs)
        self.owner_1.make_car_available('Speed Racer')
        self.assertEqual(['Mystery Machine','Speed Racer'],self.owner_1.list_of_cars)
        self.owner_1.make_car_unavailable('Mystery Machine')
        self.assertEqual(['Speed Racer'],self.owner_1.list_of_cars)
        self.owner_1.make_car_unavailable('Speed Racer')
        self.assertEqual([],self.owner_1.list_of_cars)
        

if __name__=='__main__':
    unittest.main()