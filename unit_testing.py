import unittest
from car import Car

class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car_1 = Car('Mystery Machine',
                         'Saturn',
                         'L-Series',
                         '2002',
                         'Silver',
                         '135000',
                         '0',
                         'Philadelphia',
                         'Pennsylvania')
        
        self.car_2 = Car('Knight Rider',
                         'Toyota',
                         'Camry',
                         '2009',
                         'Blue',
                         '95900',
                         '2',
                         'New York City',
                         'New York')
        
    def test_change_nickname(self):
        
        #Simple name change testing
        orig_nickname_car_1 = self.car_1.nickname
        new_name_car_1 = 'Speed Racer'
        self.car_1.nickname = new_name_car_1
        self.assertEqual(self.car_1.nickname,new_name_car_1)
        self.assertNotEqual(self.car_1.nickname,orig_nickname_car_1)

        orig_nickname_car_2 = self.car_2.nickname
        new_name_car_2 = 'My Fav Car'
        self.car_2.nickname = new_name_car_2
        self.assertEqual(self.car_2.nickname, new_name_car_2)
        self.assertNotEqual(self.car_2.nickname, orig_nickname_car_2)


        #Test character limit
        with self.assertRaises(Exception):
            self.car_2.nickname = 'ThisNameisTooManyCharactersLongforNickname!'


    def test_change_color(self):
        
        #Simple color change testing
        orig_color_car_1 = self.car_1.color
        new_color_car_1 = 'Green'
        self.car_1.color = new_color_car_1
        self.assertEqual(self.car_1.color,new_color_car_1)
        self.assertNotEqual(self.car_1.color,orig_color_car_1)

    def test_change_miles(self):
        #Simple mile change
        orig_miles_car_1 = self.car_1.miles_driven_life
        new_miles_car_1 = 230000
        self.car_1.miles_driven_life=new_miles_car_1
        self.assertEqual(self.car_1.miles_driven_life,new_miles_car_1)
        self.assertNotEqual(self.car_1.miles_driven_life,orig_miles_car_1)

        #Change miles to 0
        new_miles_car_1 = 0
        self.car_1.miles_driven_life=new_miles_car_1
        self.assertEqual(self.car_1.miles_driven_life,new_miles_car_1)

        #Try changing miles to string
        new_miles_car_2 = 'Zero miles driven'
        with self.assertRaises(ValueError):
            self.car_2.miles_driven_life = new_miles_car_2
    
        #Try changing miles to negative
        new_miles_car_2 = -999
        with self.assertRaises(ValueError):
            self.car_2.miles_driven_life = new_miles_car_2

        #Change miles to float
        new_miles_car_2 = 201012.5
        with self.assertRaises(ValueError):
            self.car_2.miles_driven_life = new_miles_car_2


    def test_increase_miles(self):
        pass

    def test_change_accidents(self):
        pass

    def increase_accidents(self):
        pass

    def change_city(self):
        pass

    def change_state(self):
        pass

if __name__=='__main__':
    unittest.main()