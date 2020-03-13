#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10"""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being .5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, .5)

    def test_unique_product_explode(self):
        """Test a unique products explode method"""
        prod = Product('Test Product', 100, 50, 3)
        # flammability * weight = exposive
        # 50 * 3 = 150
        # explode() should return "...BABOOM!!"
        self.assertEqual(prod.explode(), "...BABOOM!!")

    def test_unique_product_stealability(self):
        """Test a unique products stealability method"""
        prod = Product('Test Product', 100, 2000, 2)
        # price * weight = stealability
        # 100 / 2000 = .05
        # stealability() should return "Not so stealable..."
        self.assertEqual(prod.stealability(), "Not so stealable...")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports work as desired."""
    def test_default_num_products(self):
        """Test the default number of products is 30 when generating products"""
        list_of_products = generate_products()
        self.assertEqual(len(list_of_products), 30)

    def test_legal_names(self):
        """Checking that product names match the lists of possible names"""
        list_of_products = generate_products()
        for product in list_of_products:
            words = str.split(product.name)
            adjective = words[0]
            noun = words[1]

            self.assertIn(noun, NOUNS)
            self.assertIn(adjective, ADJECTIVES)


if __name__ == '__main__':
    unittest.main()
