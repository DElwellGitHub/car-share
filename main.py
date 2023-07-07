from car import Car

def main():
    kwargs = {'nickname':'Mysty',
              'make':'volkswagen',
              'model':'vw bus',
              'year':'1999',
              'color':'tie dye',
              'miles_driven_life':200000,
              'accidents_life':1,
              'city':'Philadelphia',
              'state':'Pennsylvania'}
    car1 = Car(**kwargs)

    print(car1.nickname)
    print(car1.miles_driven_life)
    #print(car1.city)
    #print(car1.state)
    #print(car1.city)
    #car1.all
    #print(car1.city)
    car1.city='Boston'
    print(car1.state)

if __name__=='__main__':
    main()