import unittest
from car import Car

class TestCar(unittest.TestCase):
    
    def setUp(self):
        Car.all = []
        Car.number_of_cars = 0
        
        self.car_1 = Car('Mystery Machine',
                         'Saturn',
                         'L-Series',
                         '2002',
                         'Silver',
                         '135000',
                         '0',
                         'Philadelphia',
                         'Pennsylvania',
                         12.5)
        
        self.car_2 = Car('Knight Rider',
                         'Toyota',
                         'Camry',
                         '2009',
                         'Blue',
                         '95900',
                         '2',
                         'New York City',
                         'New York',
                         14.5)
        
    def tearDown(self):
        pass

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

        #Try changing to a name that is already used
        with self.assertRaises(Exception):
            self.car_1.nickname = 'My Fav Car'

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

        #Try changing miles to float
        new_miles_car_2 = 201012.5
        with self.assertRaises(ValueError):
            self.car_2.miles_driven_life = new_miles_car_2


    def test_increase_miles(self):
        #Simple miles increase
        orig_miles_car_1 = self.car_1.miles_driven_life
        miles_added_car_1 = 200
        self.car_1.increase_miles(miles_added_car_1)
        self.assertEqual(self.car_1.miles_driven_life, 
                         orig_miles_car_1 + miles_added_car_1)
        
        #Increase miles by float
        orig_miles_car_1 = self.car_1.miles_driven_life
        miles_added_car_1 = 200.2
        self.car_1.increase_miles(miles_added_car_1)
        self.assertEqual(self.car_1.miles_driven_life, 
                         orig_miles_car_1 + miles_added_car_1)

        #Try to decrease miles
        orig_miles_car_1 = self.car_1.miles_driven_life
        miles_added_car_1 = -9
        with self.assertRaises(ValueError):
            self.car_1.increase_miles(miles_added_car_1)

        #Try to add string
        orig_miles_car_1 = self.car_1.miles_driven_life
        miles_added_car_1 = '200'
        with self.assertRaises(ValueError):
            self.car_1.increase_miles(miles_added_car_1)

        #Try to add boolean
        orig_miles_car_1 = self.car_1.miles_driven_life
        miles_added_car_1 = True
        with self.assertRaises(ValueError):
            self.car_1.increase_miles(miles_added_car_1)
        
    def test_change_accidents(self):
        #Simple accidents change
        orig_accidents_car_1 = self.car_1.accidents_life
        new_accidents_car_1 = 5
        self.car_1.accidents_life=new_accidents_car_1
        self.assertEqual(self.car_1.accidents_life,
                         new_accidents_car_1)
        self.assertNotEqual(self.car_1.accidents_life,
                            orig_accidents_car_1)

        #Change accidents to 0
        new_accidents_car_1 = 0
        self.car_1.accidents_life=new_accidents_car_1
        self.assertEqual(self.car_1.accidents_life,
                         new_accidents_car_1)

        #Try changing accidents to string
        new_accidents_car_2 = 'Zero accidents'
        with self.assertRaises(ValueError):
            self.car_2.accidents_life = new_accidents_car_2
    
        #Try changing accidents to negative
        new_accidents_car_2 = -4
        with self.assertRaises(ValueError):
            self.car_2.accidents_life = new_accidents_car_2

        #Try changing accidents to float
        new_accidents_car_2 = 4.5
        with self.assertRaises(ValueError):
            self.car_2.accidents_life = new_accidents_car_2


    def increase_accidents(self):
        #Simple accidents increase
        orig_accidents_car_1 = self.car_1.accidents_life
        accidents_added_car_1 = 4
        self.car_1.increase_accidents(accidents_added_car_1)
        self.assertEqual(self.car_1.accidents_life, 
                         orig_accidents_car_1 + accidents_added_car_1)
        
        #Increase accidents by float
        orig_accidents_car_1 = self.car_1.accidents_life
        accidents_added_car_1 = 200.2
        self.car_1.increase_miles(accidents_added_car_1)
        self.assertEqual(self.car_1.miles_driven_life, 
                         orig_accidents_car_1 + accidents_added_car_1)

        #Try to decrease accidents
        orig_accidents_car_1 = self.car_1.accidents_life
        accidents_added_car_1= -9
        with self.assertRaises(ValueError):
            self.car_1.increase_accidents(accidents_added_car_1)

        #Try to add string
        orig_accidents_car_1 = self.car_1.accidents_life
        accidents_added_car_1 = '200'
        with self.assertRaises(ValueError):
            self.car_1.increase_miles(accidents_added_car_1)

        #Try to add boolean
        orig_accidents_car_1 = self.car_1.accidents_life
        accidents_added_car_1 = True
        with self.assertRaises(ValueError):
            self.car_1.increase_miles(accidents_added_car_1)

    def change_city(self):
        #Simple city change
        orig_city = self.car_1.city
        new_city = 'New York City'
        self.car_1.city = new_city
        self.assertEqual(self.car_1.city, new_city)

        #Check to ensure that state changes
        orig_city = self.car_1.city
        new_city = 'Boston'
        self.car_1.city = new_city
        self.assertEqual(self.car_1.state,'Massachusetts')

        #Change to invalid city
        orig_city = self.car_1.city
        new_city = 'Kings Landing'
        with self.assertRaises('Exception'):
            self.car_1.city = new_city

    def change_state(self):
        #Simple state change
        new_state = 'New York'
        self.car_1.state = new_state
        self.assertEqual(self.car_1.city, new_state)

        #Check to ensure that city changes
        new_state = 'Pennsylvania'
        self.car_1.state = new_state
        self.assertEqual(self.car_1.city,'Philadelphia')

        #Change to invalid state
        new_state = 'Westeros'
        with self.assertRaises('Exception'):
            self.car_1.stat = new_state

    def test_all_attribute(self):
        #Test that "all" attribute works fine
        self.assertEqual(Car.all, self.car_1.all,self.car_2.all)

    def test_num_cars(self):
        '''
        Test that number of cars classs attribute works fine
        '''
        self.assertEqual(2,
                         Car.number_of_cars)
        self.assertEqual(2,
                         self.car_1.number_of_cars,
                         self.car_2.number_of_cars)

if __name__=='__main__':
    unittest.main()