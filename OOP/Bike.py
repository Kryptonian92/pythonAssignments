class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "Bike's Price:",self.price
        print "Maximum Speed:",self.max_speed
        print "Total Miles:",self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles = abs(self.miles - 5)
        return self

bike = Bike(200,"25mph")
bike.ride().ride().ride().reverse().displayInfo()
print "End First Instance"
print""
bike2 = Bike(300,"30mph")
bike2.ride().ride().reverse().reverse().displayInfo()
print "End Second"
print""
bike3 = Bike(400,"40mph")
bike3.reverse().reverse().reverse().displayInfo()
print "End Third"





class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold!"
        return self
    def add_tax(self, tax):
        print self.price + self.price*tax
        return self
    def Return(self, reason):
        if reason == "defective":
            self.status = "Defective"
            self.price = 0
            return self
        elif reason == "in box, like new":
            self.status = "For sale"
            return self
        elif reason == "opened":
            self.status = "Used"
            self.price = self.price*.8
            return self
    def display_info(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight, "lbs."
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
product1 = Product(120, "Blu-Ray Player", 7, "Sony", 40)
product2 = Product(1200, "Television", 95, "Sony", 400)
product3 = Product(25, "Book", 12, "Random House", 7)
product4 = Product(1500, "Mattress", 100, "Sealy", 300)
product1.add_tax(.07).display_info()
product2.sell().Return("defective").display_info()
product3.sell().Return("in box, like new").display_info()
product4.sell().Return("opened").display_info()
