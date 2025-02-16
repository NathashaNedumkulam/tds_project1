from datetime import datetime

# Path to the input and output files
input_file = 'C:/data/dates.txt'
output_file = 'C:/data/dates-wednesdays.txt'

# Read the dates from the file
with open(input_file, 'r') as f:
    dates = f.readlines()

# Function to parse the date in multiple formats
def parse_date(date_str):
    for fmt in ['%Y-%m-%d', '%Y/%m/%d %H:%M:%S']:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None

# Count the number of Wednesdays
wednesday_count = sum(1 for date in dates if parse_date(date) and parse_date(date).weekday() == 2)

# Write the result to the output file
with open(output_file, 'w') as f:
    f.write(str(wednesday_count))
