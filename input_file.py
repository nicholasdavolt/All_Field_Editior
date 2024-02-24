import csv


def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        results = []
        for row in csv_reader:
            results.append(", ".join(row))
        return results
        