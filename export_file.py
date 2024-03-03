import csv

def export_results (records):
    with open('export.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["proc_id", "rev_id","hash","custodian","path","all_custodian","all_path","Custodian_Removed"])

        for record in records:
            if len(record.rev_id) > 0:
                writer.writerow([record.proc_id,
                                 record.rev_id,
                                 record.hash,
                                 record.custodian,
                                 record.path,
                                 record.all_custodian,
                                 record.all_path,
                                 record.removed_custodian])
                