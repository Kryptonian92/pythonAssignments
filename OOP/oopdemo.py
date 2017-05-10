class Furniture(object):
    pass

class Table(Furniture):
    def __init__(self, length, color):
        self.legs = "4"
        self.color = color
        self.material = length

table1 = Table(10, "white")
table2 = Table(20, "black")
print table1.legs
print table1.color
print table1.material
print table1.length
print table2.color
print table2.length



def addition():
    return 5+5
