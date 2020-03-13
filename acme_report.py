# acme_report.py
from acme import Product
import random

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(number_of_products=30):
    """
    Generates a number of random products.
    The default number is 30, but can be changed by passing
    an integer as an argument.
    """
    list_of_products = []

    for product in range(1, (number_of_products + 1)):
        noun = random.choice(NOUNS)
        adjective = random.choice(ADJECTIVES)
        name = adjective + " " + noun
        price = random.randint(5, 101)
        weight = random.randint(5, 101)
        flammability = random.uniform(0, 2.5)

        product = Product(name, price, weight, flammability)
        list_of_products.append(product)

    return list_of_products


def inventory_report(product_list):
    """
    Takes a list of products as argument and returns the
    number of unique names and average price, weight, and
    flammability.
    """
    # Unique products
    unique_list = []
    for product in product_list:
        if product.name not in unique_list:
            unique_list.append(product.name)

    number_of_unique_product_names = len(unique_list)

    # Mean price, weight, and flamability
    total_price = 0
    total_weight = 0
    total_flammability = 0

    for product in product_list:
        total_price = total_price + product.price
        total_weight = total_weight + product.weight
        total_flammability = total_flammability + product.flammability

    average_price = total_price / len(product_list)
    average_weight = total_weight / len(product_list)
    average_flammability = total_flammability / len(product_list)

    # Building report
    message = ("\nACME CORPORATION OFFICIAL INVENTORY REPORT",
                "\nUnique product names: ", number_of_unique_product_names,
                "\nAverage price: ", average_price, "\nAverage weight: ",
                average_weight, "\nAverage flammability: ",
                average_flammability)
    return print(message)


if __name__ == '__main__':
    inventory_report(generate_products())
