"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.

"""

def main():

    sales_report = {}

    f = open("sales_report.csv")
    for line in f:
        line = line.rstrip()
        entries = line.split(",")
        salesperson = entries[0]
        melons = int(entries[2])

        # if salesperson in sales_report:
        #     sales_report[salesperson] += melons
        # else:
        #     sales_report[salesperson] = melons

        sales_report[salesperson] = sales_report[salesperson] + melons if salesperson in sales_report else melons

    for salesperson, melons in sales_report.items():
        print salesperson, "sold", melons


if __name__ == "__main__":
    (main())