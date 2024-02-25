from operator import attrgetter
def sort_records(record_list, specs):
    for key, reverse in reversed(specs):
        record_list.sort(key = attrgetter(key), reverse=reverse)


def collate_custodians(record_list):
    unique_cust = set()

    for record in record_list:
        if record.custodian not in unique_cust:
            unique_cust.add(record.custodian)
    return unique_cust
    
    
