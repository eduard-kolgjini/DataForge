# DataForge
DataForge is a versatile test data generation tool designed for software testers, developers, and data engineers who need large amounts of randomized data for testing purposes.

## Features
-Generate random data for fields such as names, emails, addresses, phone numbers, and credit card numbers.
-Supports output to CSV and JSON formats.
-Command-line interface with customizable field selection.
-Prettify JSON output option.
-Customizable CSV delimiters for flexible data export.

## Installation
Install the required dependencies: pip install -r requirements.txt

## Usage
Generate 100 records and export to CSV with default fields:
```bash
python src/dataforge.py --count 100 --format csv
```

Generate 50 records with custom fields (name, email, address) and export to CSV:
```bash
python src/dataforge.py --count 50 --fields name email address --format csv
```

Generate 50 records and export to JSON with prettified output:
```bash
python src/dataforge.py --count 50 --format json --pretty
```
Export CSV with a custom delimiter:
```bash
python src/dataforge.py --count 50 --fields name email --delimiter ";"
```

## Options
- `--count`: Number of records to generate (default: 100).
- `--format`: Export format (`csv` or `json`).
- `--fields`: Fields to include in the generated data (space-separated values).
  - Available fields: `name`, `email`, `address`, `phone_number`, `credit_card`.
- `--pretty`: Prettify JSON output (applies to JSON format only).
- `--delimiter`: CSV delimiter (applies to CSV format only, default: `,`).

## Running Tests

To run the unit tests:
```bash
python -m unittest discover tests
```

