# Object Oriented Programming
# Class (Tax) & Object
"""
        class Tax:
            taxrate = 0.07 # Class Attribute

            @staticmethod
            def caltax(productprice): # Instance Method
                return Tax.taxrate * productprice
"""
from tkinter.font import names


# ปรเภทแอทริบิวต์ (Taxrate)
# ประเภทเทธอด (Caltax)
# Access Modifier Public, Private, Protected
# Encapsulation
# Inheritance & Polymorphism

class Tank:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo
    def add_ammo(self, ammo):
        if self.ammo + ammo <= 10:
            self.ammo += ammo
    def fire_ammo(self):
        if self.ammo > 0:
            self.ammo -= 1

firstTank = Tank('F1s', 4)
firstTank.add_ammo(4)
print(firstTank.ammo)
firstTank.fire_ammo()
firstTank.fire_ammo()
firstTank.fire_ammo()
firstTank.fire_ammo()
firstTank.fire_ammo()
print(firstTank.ammo)