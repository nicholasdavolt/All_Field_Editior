from operator import attrgetter
from os import system, name
def sort_records(record_list, specs):
    for key, reverse in reversed(specs):
        record_list.sort(key = attrgetter(key), reverse=reverse)


def collate_custodians(record_list):
    unique_cust = set()

    for record in record_list:
        if record.custodian not in unique_cust:
            unique_cust.add(record.custodian)
    return unique_cust

def console_clear():
    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

def collect_cust_exclusions(custodians):
    exclusions = set()
    collect = True
    while collect:
        print("Custodians Present:")
        for cust in custodians:
            print(cust)
        if len(exclusions) > 0:
            print("Exclusions Present:")
            for exclusion in exclusions:
                print(exclusion)
        exclusion_input =  input("Add Exclusions (Y/N):").lower()

        if exclusion_input == "y" or exclusion_input == "n":
            if exclusion_input == "n":
                break
            else:

        
                
                custodian = input("Enter Custodian to exclude:")
                if custodian in exclusions:
                    print("Custodian already present in exclusion list")
                    console_clear()

                else:
                    exclusions.add(custodian)
                    console_clear()
                
        else:
            print("Invalid Entry")



            

    return exclusions

def exclude_cust_info(records, exclusions):

    for record in records:
        if record.custodian in exclusions:
            record.custodian = None
            record.path = None
            record.removed_custodian = True

def collate_all_custs(records):
    all_cust = {}

    for record in records:
        if record.hash in all_cust:
            if record.custodian:
                if record.custodian not in all_cust[record.hash]:
                    all_cust[record.hash].append(record.custodian)
        else:
            if record.custodian:
                all_cust[record.hash] = [record.custodian]

        

    return all_cust

def collate_all_paths(records):
    all_paths = {}
     
    for record in records:
        if record.hash in all_paths:
            if record.custodian:
                if record.path not in all_paths[record.hash]:
                    all_paths[record.hash].append(record.path)
        else:
            if record.custodian:
                all_paths[record.hash] = [record.path]

        

    return all_paths

def populate_all_path_cust(records, cust_by_hash, path_by_hash):

    for record in records:
        if record.hash in cust_by_hash:
            record.all_custodian = cust_by_hash[record.hash]
        if record.hash in path_by_hash:
            record.all_path = path_by_hash[record.hash]
    



    
            

    
    
