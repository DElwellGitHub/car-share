# <i>Quick Car</i>: a car share service

## Overview
The purpose of this project was to practice objected oriented programming (OOP) in Python. Through this project, I put into practice OOP principles such as inheritance, encapsulation and abstraction with the aim of creating classes that will be useful for <i>Quick Car</i>, a fictional car share service I designed. 

In my personal life, I often use hourly car share servies like Zipcar or Getaround. These services let you reserve a car that you can rent by the hour. Although anyone who signs up and meets the eligibility criteria can rent on these platforms, some, such as Getaround, actually allow car owners to rent out their own personal cars, which allows them to earn money in a way that home owners use Airbnb to rent their properties.

Using Getaround as a model, I created a package (carshare_classes) that contains several classes that allow people to create an account (as either owners or renters), make their car available to rent or rent someone else's car. To avoid errors in my code, I set up many different unit tests, intended to capture a myriad of potential bugs. By running the main.py script, you can see how simple it is to set up objects for owners, renters and cars, and how one can easily create these objects from an upload of csv data.

### Car class
The Car class defines the methods and attributes related to cars, which owners can rent out to renters.
- Attributes:
    - <b>Nickname</b>: a car must have a unique nickname, which serves as a unique identifier. Nickname must be 30 characters or less.
    - <b>Make</b>, <b>Model</b>, and <b>Color</b>: these are basic attributes so that renters understand what kind of car they are renting.
    - <b>Year</b>: car must be 1980 or later. It also cannot be a year set more than one year in the future.
    - <b>Miles Driven Life</b>: the number of miles on the odometer of the car. Must be zero or greater.
    - <b>Accidents Life</b>: the number of accidents the car has been involved in throughout its life. Must be zero or greater.
    - <b>City</b> and <b>State</b>: a car must have its location defined. Only participating cities (Boston, Philadelphia and New York) and their respective states are allowable.
    - <b>Cost per hour</b>: how much it costs to rent the car per hour.
    - <b>Owner</b>: the owner of the car.
- Important Methods:
    - <b>Instantiate from csv</b>: allows someone to upload a series of cars from a csv file rather than instantiating each one by one.
    - <b>Increase miles</b>: this method increases the number of miles for a car. This is important for when the car is constantly rented, and miles are added to its odometer.
    - <b>Increase accidents</b>: similar to above, this increases the number of accidents on the car.

### Member class
The Member class represents an individual who creates an account for <i>Quick Car</i>. It is the parent of both Owner and Renter, and its methods are inherited by its child classes. By creating this parent class, we cut down on needing to duplicate a lot of code between Owner and Renter classes. 
- Attributes:
    - <b>First Name</b> and <b>Last Name</b>: name of person who is creating the account.
    - <b>Date of Birth</b>: the person's birthday. They must be 18 years or older in order to create an account.
    - <b>Email</b>: the email of the member serves as their unique identifier. Email must follow a standard format (e.g. john.smith@gmail.com).
    - <b>Account Balance</b>: the amount which the person either has as credit in their account or which they owe. A renter would normally have a negative balance, while an owner would likely have a positive balance.
- Important Methods:
    - <b>Instantiate from csv</b>: similar to Car class, this allows someone to upload a csv of Members, Owners or Renters and create accounts for them quickly.
    - <b>Number of people</b>: shows number of either Members, Owners or Renters who have been created.
    - <b>Update Account balance</b>: increase or decreases the member's account balance, based on whether they rented a car or whether someone rented their car.

### Owner class
The Owner class represents an individual who will rent out their car on <i>Quick Car</i>. This class is a child of Member, which means it inherits Member's attributes and methods.
- Attributes:
    - All attributes from Member
    - <b>Number of Cars</b>: a count of number of cars that the owner has registered.
    - <b>List of Cars</b>: a list of the cars that the owner has registered.
    - <b>Latest Car Added</b>: the last car that the owner has registered.

- Important Methods:
    - All methods from Member
    - <b>Add car</b>: let's owner add a car (i.e. register it to their account).
    - <b>Make car available</b>: let's owner rent out the car to interested renters.
    - <b>Make car unavailable</b>: let's an owner make a previously available car be unavailable, so that renter's cannot use it.

### Renter class
The Renter class represents an invidual who will rent a car on <i>Quick Car</i>. This class is a child of Member, which means it inherits Member's attributes and methods.
- Attributes:
    - All attributes from Member
    - <b>Accidents</b>: the number of accidents in which a renter has been involved in.
    - <b>Current Car</b>: the car which the renter currently has resevered or rented.
    - <b>Last Car</b>: the latest car which the renter has returned.

- Important Methods:
    - All methods from Member
    - <b>Rent car</b>: let's renter rent a car. They must set a start time and return time for their reservation.
    - <b>Return car</b>: let's renter return a car. Upon returning they will be charged cost of hour of car by the hours it was taken out. A late return or accident will incur additional chargs.
    - <b>Increase accidents</b>: increments the number of accidents that the renter has had.

## Final Note
Although real-life car sharing services will have a much more sophisticated design, this project was intended to be a simiplified framework to practice OOP principles. Through this experience, I learned more about how to design code in a more simple way that avoids repetition, abstracts nuance and restricts users from editing immutable attributes (e.g. email or date of birth). As I continue to code in future projects, I hope to continue improving these skills, so that I write cleaner code that is easy to read and debug.