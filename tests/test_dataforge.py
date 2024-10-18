# tests/test_dataforge.py

import unittest
from src.dataforge import DataForge

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

if __name__ == '__main__':
    unittest.main()
