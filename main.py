from BarcodeReading import *

def main():
    while True:
        print("Menu: Read(R), Check(C), Exit(E)")
        x = input("Type: ")
        if x == "Read" or x == "R":
            Read()
        elif x == "Check" or x == "C":
            print("Check")
        elif x == "Exit" or x == "E":
            break
        else:
            print("[ERROR] INCORRECT")

if __name__ == "__main__":
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass