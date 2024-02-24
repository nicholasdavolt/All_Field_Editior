import csv
from record_object import Record_Object


def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        results = []
        for row in csv_reader:
            results.append(row)
        return results
    
def create_record(row):
    proc_id = row[0]
    rev_id = row[1]
    hash = row[2]
    cust = row[3]
    path = row[4]

    record = Record_Object(proc_id, rev_id, hash, cust, path)
    return record
        