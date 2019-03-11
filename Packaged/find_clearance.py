# Created by Amandeep at 3/10/2019
# "We are drowning in information, while starving for wisdom - E. O. Wilson"

# !/usr/bin/python

import sys
import os.path
from path_finder import PathFinder

def main(argv):
    if len(argv) == 1:
        image_path = argv[0]
        if os.path.isfile(image_path):
            import time
            start = time.time()
            PathFinder().get_next_path(image_path)
            end = time.time()
            print("Time taken to execute(in seconds) = " + str(end - start))

        else:
            raise Exception('User Error - File not located at the location mentioned in argument')
    else:
        raise Exception('User Error - Invalid number of arguments passed!!')


if __name__ == "__main__":
    main(sys.argv[1:])
