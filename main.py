#!/usr/bin/env python

import sys

if __name__ == '__main__':
    
    if sys.version_info < (3, 6):
        sys.exit("requires Python 3.6 or higher")
    try:
        from src import app
        app.main()
    except Exception as e:
        print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     print("Cool~")
