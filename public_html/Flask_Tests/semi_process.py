import time
import sys

def main(argv):
    print("entered here")
    time.sleep(float(argv[0]))
    with open("diditwork.txt", "w") as ofile:
        ofile.write("yes1!!")
    print("leaving here")

if __name__ == "__main__":
    print("starting script")
    main(sys.argv[1:])
    print("ending script")

