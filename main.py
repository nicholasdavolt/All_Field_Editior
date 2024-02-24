import os
from input_file import read_csv, create_record
from record_object import Record_Object
from data import sort_records


def main():
    file_path = input("Enter your path:")
    

    while not os.path.isfile(file_path):
        file_path = input("Filepath not valid, Re-Enter:")
    
    print("File exists, beginning import")

    csv_contents = read_csv(file_path)

    record_objects = []

    for i in range(1, len(csv_contents)):
        row = csv_contents[i]        
        record_objects.append(create_record(row))


    
    sort_records(record_objects, (('hash', False), ('rev_id', True)))

    for record in record_objects:
        record.print_record()
    

    


        
    
       
    

main()