#!/usr/bin/env python

import sys

# Remember the image with the hidden is always called "Cover.png"
if __name__ == '__main__':
    
    # Check for python version 3.6 or higher
    if sys.version_info < (3, 6):
        sys.exit("vangonography requires Python 3.6 or higher")
        
    try:
        from src import app
        print("Impoetred a")
        app.main()
    except Exception as e:
        print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     print("Cool~")
