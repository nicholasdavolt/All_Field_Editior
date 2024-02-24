

class Record_Object:

    def __init__(self, proc_id, rev_id, hash, cust, path):
        self.proc_id = proc_id
        self.rev_id = rev_id
        self.hash = hash
        self.custodian = cust
        self.path = path
        self.all_custodian = []
        self.all_path = []

    def print_record(self):
        print(f"{self.proc_id}, {self.rev_id}, {self.hash}, {self.custodian}, {self.path}, {self.all_custodian}, {self.all_path}")
