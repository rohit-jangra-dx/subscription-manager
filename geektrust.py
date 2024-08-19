import sys
from src.inputoutput.inputparser import InputParser

def main():
    if(len(sys.argv) < 1):
        raise ValueError("No input file path given!")
    
    file_path = sys.argv[1]

    obj = InputParser(file_path)
    user = obj.parse()    
    print(user.total_price)
    

if __name__ == "__main__":
    main()