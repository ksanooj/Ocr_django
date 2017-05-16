import csv
import os

module_dir = os.path.dirname(__file__)
data_path = os.path.join(module_dir, 'data')

def csv_rows(filename):
    with open(os.path.join(data_path,filename), "rb") as csvfile:
        next(csvfile)
        datareader = csv.reader(csvfile)
        for row in datareader:
            yield row


