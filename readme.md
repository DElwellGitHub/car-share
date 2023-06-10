## Car share system
Purpose of this project is to use object oriented programming to create a car share system.

### Classes
- Car
    - GasCar
    - EV

- CarOwner
    - Company (can have many cars)
    - Individual (can only have one car)

- CarRenter
    - Company (can rent multiple cars and have multiple individuals)
    - Individual (can only rent one car and one individual)

### Attributes
- GasTank (what % full is gas tanks)
- EVCharge (how charged is the EV)
- MilesDrivenTrip (how many miles has the vehicle been driven on trip)
- MilesDrivenLife (how many miles has the vehicle been driven on life)
- AccidentsTrip (any accidents on trip)
- AccidentsLife (any accidents on life)
- Year (year of car)
- Make (make of car)
- Model (model of car)
- Color (color of car)
- City (city where car is located)
- State (state where car is located)

### Methods
- RentCar
    - Individuals can rent one.
    - Companies can rent multiple.

- ReturnCar
    - returning a car

- AddCar
    - CarOwner can add car to their invy

- RemoveCar
    - CarOwner can remove car from their invy

- PayBill
    - CarRenter can pay bill

- CalculateBill
    - Car bill calculated




