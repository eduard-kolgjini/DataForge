# src/dataforge.py

from faker import Faker
import csv
import json

# Initialize the Faker instance
fake = Faker()

class DataForge:
    def __init__(self):
        self.fake = Faker()

    def generate_name(self):
        return self.fake.name()

    def generate_email(self):
        return self.fake.email()

    def generate_address(self):
        return self.fake.address()

    def generate_data(self, count=10):
        data = []
        for _ in range(count):
            entry = {
                'name': self.generate_name(),
                'email': self.generate_email(),
                'address': self.generate_address()
            }
            data.append(entry)
        return data

    def export_to_csv(self, filename, data):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)

    def export_to_json(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    forge = DataForge()
    data = forge.generate_data(count=100)  # Generate 100 entries

    # Export data to CSV and JSON
    forge.export_to_csv("test_data.csv", data)
    forge.export_to_json("test_data.json", data)

    print("Data generated and exported successfully!")
