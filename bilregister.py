my_cars = []
my_mileage = []
my_brands = []
my_color = []


class Car:
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        print(self.brand)

    def set_brand(self, new_brand):
        self.brand = new_brand

    def get_color(self):
        print(self.color)

    def get_mileage(self):
        print(self.mileage)

    def set_color(self, new_color):
        self.color = new_color

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage


for bilar in my_cars:
    print(bilar)

# ----------Huvudprogram----------
a_car = Car('porsche', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand("volvo")
a_car.get_brand()
b_car = Car('Lamborghini', 'vit', 199)
b_car.get_brand()
b_car.get_color()
b_car.get_mileage()
c_car = Car('ferrari', 'röd', 1032)
c_car.get_brand()
c_car.get_color()
c_car.get_mileage()
d_car = Car('bentley', 'silver', 487)
d_car.get_brand()
d_car.get_color()
d_car.get_mileage()

my_cars.append(a_car)
my_cars.append(b_car)
my_cars.append(c_car)
my_cars.append(d_car)


#inte klar riktigt här 


def meny():
    svar = input("1 för att se märke, 2 för att se färg, 3 för att se miltal")
    sorted_list = []
    if svar == "1":
        for car in my_cars:
            sorted_list.append(car.get_brand)
        sorted_list.sort()
        for car in sorted_list:
            print(car)
    elif svar == "2":
        for car in my_cars:
            sorted_list.append(car.get_color)
        sorted_list.sort()
        for car in sorted_list:
            print(car)
    elif svar == "3":
        for car in my_cars:
            sorted_list.append(car.get_mileage)
        sorted_list.sort()
        for car in sorted_list:
            print(car)
    else:
        print("du är fan dum i huvudet")


meny()

