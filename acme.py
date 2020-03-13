# acme.py
import random


class Product():
    """
    Product object with name, price, weight,
    and flammability.
    """

    def __init__(self, name, price=10, weight=20, flammability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(999999, 9999999)

    def stealability(self):
        """Returns a string based on the products stealability."""
        stealability = self.price / self.weight
        if (stealability < 0.5):
            return "Not so stealable..."
        elif ((stealability >= 0.5) & (stealability < 1.0)):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Returns a string based on the products explosiveness"""
        explosive = self.flammability * self.weight
        if (explosive < 10):
            return "...fizzle."
        elif ((explosive >= 10) & (explosive < 50)):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """
    Boxing Glove object that inherits from the Product class.
    Default weight is 10. Explode method returns a constant.
    New method punch returns a string based on weight.
    """

    def __init__(self, name, price=10, weight=10, flammability=.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(999999, 9999999)

    def explode(self):
        """Returns a constant"""
        return "...it's a glove."

    def punch(self):
        """Returns a string based on the BoxingGlove's weight"""
        if (self.weight < 5):
            return "That tickles."
        elif ((self.weight >= 5) & (self.weight < 15)):
            return "Hey that hurt!"
        else:
            return "OUCH!"
