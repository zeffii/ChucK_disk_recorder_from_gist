#import time
import sys
from chuck_process import take_input

def main(argv):
    print("entered here")
    take_input(*argv)
    print("leaving here")

if __name__ == "__main__":
    print("starting script")
    main(sys.argv[1:])
    print("ending script")

