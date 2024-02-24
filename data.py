from operator import attrgetter
def sort_records(record_list, specs):
    for key, reverse in reversed(specs):
        record_list.sort(key = attrgetter(key), reverse=reverse)
    
    
