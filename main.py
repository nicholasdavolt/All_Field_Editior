import os

def main():
    file_path = input("Enter your path:")
    

    while not os.path.isfile(file_path):
        file_path = input("Filepath not valid, Re-Enter:")
    
    print("File exists, beginning validation")
    
        
       
    

main()