class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand

    def get_color(self):
        print(self.color)


    def get_mileage(self):
        print(self.mileage)



# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
a_car = Car('', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('')
a_car.get_brand()
b_car = Car('Lamborghini', 'vit', 199999999)
b_car.get_brand()       # får vi märket på den nya bilen
b_car.get_color()       # får vi färgen
b_car.get_mileage()     #får vi miltalet
b_car.set_brand("Ferrari")       # får vi nu ett nytt bilmärke
b_car.get_brand()       # får vi bilmärket igen

# ----------Huvudprogram----------
