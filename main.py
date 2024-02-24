import os
from input_file import read_csv


def main():
    file_path = input("Enter your path:")
    

    while not os.path.isfile(file_path):
        file_path = input("Filepath not valid, Re-Enter:")
    
    print("File exists, beginning import")

    csv_contents = read_csv(file_path)

    for row in csv_contents:
        print(row)
    
       
    

main()