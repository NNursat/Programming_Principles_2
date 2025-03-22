import os

def check_path(path):
    
    if os.path.exists(path): 
        print(f" The path exists: {path}")
        
        directory = os.path.dirname(path)
        filename = os.path.basename(path)
        
        print(f" Directory: {directory}")
        print(f" Filename: {filename}")
    
    else:
        print(f" The path does not exist: {path}")

# Example: Replace with your actual path
path_to_check = r"C:\Users\Nursat\Desktop\Study\PP2\Lab 6\dir-and-files\test.txt"
check_path(path_to_check)
