from carshare_classes.car import Car
from carshare_classes.owner import Owner
from carshare_classes.renter import Renter
import datetime as dt
import csv

def instantiate_members(file_path,file_name,class_):
    '''
    Read from appropriate csv (Owner, Renter, Car) all instances in file.
    Then dynamically assign each instance to a variable with unique
    number (e.g. owner_1, owner_2, renter_1, renter_2, etc.).
    '''
    class_.instantiate_from_csv(f'{file_path}/{file_name}')

    for i in range(class_.number_of_people):
        class_num = str(f'{class_.__name__}_'.lower()+str(i+1))
        globals().__setitem__(class_num,
                              class_.all_instances[i])
        
    print(f'{class_.number_of_people} '+f'{class_.__name__}s '.lower() + 'registered.')
        
def owner_add_all_cars(owner_var):
    '''
    Add all cars in csv file to owner.
    '''
    with open ('/home/ubuntu/car-share/csv/cars.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            owner_var.add_car(**row)

if __name__=='__main__':    
    #Instantiate renters from csv
    instantiate_members(file_path = '/home/ubuntu/car-share/csv',
                        file_name='renters.csv',
                        class_=Renter)
    
    #Instantiate owners from csv
    instantiate_members(file_path = '/home/ubuntu/car-share/csv',
                        file_name='owners.csv',
                        class_=Owner)


    #Add all cars in csv to owner_1
    owner_add_all_cars(owner_1)

    #Make a car available to rent
    owner_1.make_car_available(owner_1.latest_car_added.nickname)
    print(f'{owner_1.first_name} {owner_1.last_name} made their car "{owner_1.latest_car_added.nickname}" available to rent.')

    #Have a renter rent it
    start_time = dt.datetime(year=2023,month=7,day=1,hour=12,minute=30)
    return_time = dt.datetime(year=2023,month=7,day=1,hour=18,minute=0)

    renter_1.rent_car(car_rented =owner_1.latest_car_added,
                      datetime_start = start_time,
                       datetime_return = return_time)
    print(f'{renter_1.first_name} {renter_1.last_name} rented {renter_1.current_car}.nickname')

    #Have a renter return it
    renter_1.return_car(miles_driven=140,
                       accidents=0,
                       real_time_return = False)
    print(f'{renter_1.first_name} {renter_1.last_name} returned {renter_1.last_car}.')
    print(f'{renter_1.first_name} {renter_1.last_name} has an account balance now of {renter_1.account_balance}')