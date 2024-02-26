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
            

    
    
