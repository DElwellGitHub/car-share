from carshare_classes.car import Car
from carshare_classes.owner import Owner
from carshare_classes.renter import Renter
import datetime as dt

def main():
    Car.instantiate_from_csv('cars.csv')


    #Read in all owners' data from a csv
    Owner.instantiate_from_csv('owners.csv')


    #Dynamically assign each owner instance to a variable with unique number (i.e. owner_1, owner_2, etc.)
    for i in range(Owner.number_of_people):
        owner_num = str('owner_'+str(i+1))
        globals().__setitem__(owner_num,Owner.all_instances[i])

    owner_1 = Owner.all_instances[0]
    print(owner_1.first_name)
    print(owner_4.email)

if __name__=='__main__':
    main()