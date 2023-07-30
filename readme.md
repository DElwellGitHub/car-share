# <i>Quick Car</i>: a car share service

### Overview
The purpose of this project was to practice objected oriented programming (OOP) in Python. Through this project, I put into practice OOP principles such as inheritance, encapsulation and abstraction with the aim of creating classes that will be useful for <i>Quick Car</i>, a fictional car share service I designed. 

In my personal life, I often use hourly car share servies like Zipcar or Getaround. These services let you reserve a car that you can rent by the hour. Although anyone who signs up and meets the eligibility criteria can rent on these platforms, some, such as Getaround, actually allow car owners to rent out their own personal cars, which allows them to earn money in a way that home owners use Airbnb to rent their properties.

Using Getaround as a model, I created a package (carshare_classes) that contains several classes that allow people to create an account (as either owners or renters), make their car available to rent or rent someone else's car. To avoid errors in my code, I set up many different unit tests, intended to capture a myriad of potential bugs. By running the main.py script, you can see how simple it is to set up objects for owners, renters and cars, and how one can easily create these objects from an upload of csv data.

### Classes
- Car


- Owner

- Renter

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




