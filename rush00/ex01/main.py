from checkmate import checkmate
import sys, os

def main():
    argv = sys.argv
    if len(argv) == 1:
        print("No input")
    elif len(argv) == 2 and argv[1] == "--all":
        files = os.listdir()
        for file in files:
            if file[-6:] == ".chess":
                print(file, end=" >>> ")
                with open(file, "r") as f:
                    board = f.read()
                checkmate(board)
    else:
        for p in argv[1:]:
            try:
                with open(p, "r") as f:
                    board = f.read()
                checkmate(board)
            except:
                print("Error")
    
if __name__ == "__main__":
    main()