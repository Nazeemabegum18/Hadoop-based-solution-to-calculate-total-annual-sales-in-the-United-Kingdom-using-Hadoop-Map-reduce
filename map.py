import sys
import io
import csv

def process_input_mapper_england_sales(line):
    """
    Process a single line of text: split the line by comma and extract year and sales if the country is England
    """
    country = line[7].strip()
    country = country.strip('"')
    if country.lower() == "united kingdom":
        year = line[20]
        sales = float(line[14].replace(",", ""))  # Remove commas from sales"
        print("%s\t%s" % (year, sales))

def main():
    # Read from standard input with specified encoding through csv reader.
    csvreader = csv.reader(sys.stdin)   
    for line in csvreader:
        # map England sales data per year
        process_input_mapper_england_sales(line)

if __name__ == '__main__':
    main()
