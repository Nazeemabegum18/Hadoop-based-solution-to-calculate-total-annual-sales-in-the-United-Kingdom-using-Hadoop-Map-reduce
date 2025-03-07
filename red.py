import sys

def reducer_find_total_sales_england():
    (last_year, total_sales) = (None, 0)
    for line in sys.stdin:
        (year, sales) = line.strip().split("\t")
        if last_year and last_year != year:
            print("%s\t%s" % (last_year, total_sales))
            (last_year, total_sales) = (year, float(sales))
        else:
            (last_year, total_sales) = (year, total_sales + float(sales))

    if last_year:
        print("%s\t%s" % (last_year, total_sales))

def main():
    reducer_find_total_sales_england()

if __name__ == '__main__':
    main()
