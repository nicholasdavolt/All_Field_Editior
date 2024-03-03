import os
from input_file import read_csv, create_record
from record_object import Record_Object
from data import sort_records, collate_custodians, collect_cust_exclusions, exclude_cust_info, collate_all_custs, collate_all_paths, populate_all_path_cust
from export_file import export_results


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

    unique_custs = collate_custodians(record_objects)



    exclude_custodians = collect_cust_exclusions(unique_custs)

    if not exclude_custodians:
        print("Continuing with no exclusions")
    else:
        print("Excluding Custodians:")

        for cust in exclude_custodians:
            print(cust)
    
    exclude_cust_info(record_objects, exclude_custodians)

    cust_by_hash = collate_all_custs(record_objects)
    path_by_hash = collate_all_paths(record_objects)

    populate_all_path_cust(record_objects, cust_by_hash, path_by_hash)

    export_results(record_objects)

    
    


    


        
    
       
    

main()