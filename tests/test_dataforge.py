import unittest
from src.dataforge import DataForge  # Import the DataForge class
import os
import json

class TestDataForge(unittest.TestCase):

    def setUp(self):
        self.forge = DataForge()

    def test_generate_name(self):
        name = self.forge.generate_name()
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)

    def test_generate_email(self):
        email = self.forge.generate_email()
        self.assertIsInstance(email, str)
        self.assertIn("@", email)

    def test_generate_phone_number(self):
        phone = self.forge.generate_phone_number()
        self.assertIsInstance(phone, str)
        self.assertGreater(len(phone), 0)

    def test_generate_credit_card(self):
        credit_card = self.forge.generate_credit_card()
        self.assertIsInstance(credit_card, str)
        self.assertGreater(len(credit_card), 0)

    def test_generate_data_with_custom_fields(self):
        data = self.forge.generate_data(count=5, fields=['name', 'email'])
        self.assertEqual(len(data), 5)
        for entry in data:
            self.assertIn('name', entry)
            self.assertIn('email', entry)
            self.assertNotIn('address', entry)

    def test_csv_export(self):
        data = self.forge.generate_data(count=5)
        self.forge.export_to_csv("test_output.csv", data)

        with open("test_output.csv", 'r') as file:
            lines = file.readlines()

        # Check that the correct number of lines is present (1 header + 5 data lines)
        self.assertEqual(len(lines), 6)

        os.remove("test_output.csv")  # Clean up after test

    def test_json_export(self):
        data = self.forge.generate_data(count=5)
        self.forge.export_to_json("test_output.json", data)
        with open("test_output.json", 'r') as file:
            json_data = json.load(file)
            self.assertEqual(len(json_data), 5)
        os.remove("test_output.json")  # Clean up after test

if __name__ == '__main__':
    unittest.main()
