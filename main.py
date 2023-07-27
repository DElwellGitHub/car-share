from carshare_classes.car import Car
from carshare_classes.owner import Owner
from carshare_classes.renter import Renter

def main():
    Car.instantiate_from_csv('cars.csv')
    Owner.instantiate_from_csv('owners.csv')
    print(Owner.all_instances[0].first_name)


if __name__=='__main__':
    main()