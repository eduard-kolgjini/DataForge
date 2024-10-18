# DataForge

DataForge is a versatile test data generation tool designed for software testers, developers, and data engineers who need large amounts of randomized data for testing purposes.

## Features
- Generate random names, emails, addresses, phone numbers, and credit card numbers.
- Supports output to CSV and JSON formats.
- Command-line interface for easy usage with custom field options.
- Customizable JSON output with a prettify option.
- Customizable CSV delimiters for flexible data export.

## Installation

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### **Usage**

To generate 100 records and export to CSV with default fields:

```bash
python src/dataforge.py --count 100 --format 
```

To generate data with only specific fields (e.g., name, email):
```bash
python src/dataforge.py --count 50 --fields name email --format csv
```

To export CSV with a custom delimiter:
```bash
python src/dataforge.py --count 50 --fields name email --delimiter ";"
```

## Running Tests

To run the unit tests:
```bash
python -m unittest discover tests
```