import csv

with open("tests/data/add.csv",newline="",encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
