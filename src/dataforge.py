import argparse
from faker import Faker
import csv
import json

class DataForge:
    def __init__(self):
        self.fake = Faker()

    def generate_name(self):
        return self.fake.name()

    def generate_email(self):
        return self.fake.email()

    def generate_address(self):
        return self.fake.address().replace('\n', ', ')

    def generate_phone_number(self):
        return self.fake.phone_number()

    def generate_credit_card(self):
        return self.fake.credit_card_number()

    def generate_data(self, count=10, fields=None):
        if not fields:
            fields = ['name', 'email', 'address', 'phone_number', 'credit_card']
        data = []
        for _ in range(count):
            entry = {}
            if 'name' in fields:
                entry['name'] = self.generate_name()
            if 'email' in fields:
                entry['email'] = self.generate_email()
            if 'address' in fields:
                entry['address'] = self.generate_address()
            if 'phone_number' in fields:
                entry['phone_number'] = self.generate_phone_number()
            if 'credit_card' in fields:
                entry['credit_card'] = self.generate_credit_card()
            data.append(entry)
        return data

    def export_to_csv(self, filename, data, delimiter=','):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=delimiter)
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)

    def export_to_json(self, filename, data, pretty=False):
        with open(filename, 'w') as file:
            if pretty:
                json.dump(data, file, indent=4)
            else:
                json.dump(data, file)

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description='Generate test data.')
    parser.add_argument('--count', type=int, default=100, help='Number of records to generate')
    parser.add_argument('--format', type=str, choices=['csv', 'json'], default='csv', help='Export format')
    parser.add_argument('--fields', type=str, nargs='+', default=['name', 'email', 'address'], 
                        help='Fields to include in the generated data (e.g., name, email, address, phone_number, credit_card)')
    parser.add_argument('--pretty', action='store_true', help='Prettify JSON output (applies to JSON format only)')
    parser.add_argument('--delimiter', type=str, default=',', help='CSV delimiter (applies to CSV format only)')

    args = parser.parse_args()

    forge = DataForge()
    data = forge.generate_data(count=args.count, fields=args.fields)

    if args.format == 'csv':
        forge.export_to_csv("test_data.csv", data, delimiter=args.delimiter)
    elif args.format == 'json':
        forge.export_to_json("test_data.json", data, pretty=args.pretty)

    print(f"Data generated and exported to {args.format.upper()} successfully!")
