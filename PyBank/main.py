import os
import csv

budget_path = os.path.join("resources","budget_data.csv")

with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter = ",")
    print(next(budget_reader))