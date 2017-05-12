class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.displayAll()
    def displayAll(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Milage:", self.milage
        print "Tax:", self.tax
        return self

BMW = Car(2000, "35mph", "Full", "15mpg")
print ""
Lambo = Car(20000, "5mph", "not Full", "105mpg")
print ""
Toyota = Car(90000, "15mph", "kind of Full", "95mpg")
print ""
Fiat = Car(2000, "25mph", "Full", "25mpg")
print ""
Porsche = Car(24000, "45mph", "Empty", "25mpg")
print ""
Ferrari = Car(2000, "35mph", "Full", "15mpg")

















#
#
#
#
#
# class Car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         if price > 10000:
#             self.tax = .15
#         else:
#             self.tax = .12
#         self.display_all()
#     def display_all(self):
#         print "Price:", self.price
#         print "Speed:", self.speed, "mph"
#         print "Fuel:", self.fuel
#         print "Mileage:", self.mileage, "mpg"
#         print "Tax:", self.tax
#         return self
# car1 = Car(200000, 435, "Full", 16)
# car2 = Car(100000, 280, "Full", 27)
# car3 = Car(75000, 210, "3/4 Tank", 45)
# car4 = Car(20000, 180, "1/2 Tank", 32)
# car5 = Car(9000, 120, "1/4 Tank", 22)
# car6 = Car(3000, 85, "Almost Empty", 12)
