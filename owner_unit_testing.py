import unittest
import datetime as dt
from owner import Owner

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
        pass
    def test_invalid_email(self):
        '''
        Test trying to create an owner with an invalid email pattern.
        '''
        pass
    def test_add_car(self):
        '''
        Test adding a car to owner's list of registered cars.
        '''
        pass
    def test_make_car_available(self):
        '''
        Test making a registered car available.
        '''
        pass
    def test_make_car_unavailable(self):
        '''
        Test making an available car unavailable.
        '''
        pass
    
if __name__=='__main__':
    unittest.main()