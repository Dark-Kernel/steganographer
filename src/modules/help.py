 # __
# (__|_ _  _  _.._  _  _ .__.._ |_  _ ._
# __)|_(/_(_|(_|| |(_)(_||(_||_)| |(/_|
 #         _|          _|    |


def banner():
    print ('''

  ()                                                      | |
  /\_|_  _   __,  __,   _  _    __   __,  ,_    __,    _  | |     _   ,_
 /  \|  |/  /  | /  |  / |/ |  /  \_/  | /  |  /  |  |/ \_|/ \   |/  /  |
/(__/|_/|__/\_/|/\_/|_/  |  |_/\__/ \_/|/   |_/\_/|_/|__/ |   |_/|__/   |_/
              /|                      /|            /|
              \|                      \|            \|

                        |v1.0| \033[1;91mhttps://dark-kerne.web.app\033[0m

    \033[1m\033[93mWe hide, you seek, it's art, don't peek.\033[0m\033[0m\n\n''')





def helpmenu():
    optional_group = parser.add_argument_group('Optional arguments')
    optional_group.add_argument("-l", "--log", dest="log", action="store_true", default=False, help="Log file for the program (default: False)")
    optional_group.add_argument("-cli", dest="cli", action="store_true", default=False, help="Run the program in CLI mode")
    optional_group.add_argument("-i", "--input", dest="input", type=str, help="input file")
    optional_group.add_argument("-o", "--output", dest="output", type=str, metavar="OUTPUT_DIR", help="Output directory for the modified file")
    optional_group.add_argument("--encrypt", dest="encrypt", action="store_true", default=False, help="Encrypt the data before hiding it (default: False)")
    optional_group.add_argument("--decrypt", dest="decrypt", action="store_true", default=False, help="Decrypt the data after revealing it (default: False)")
    optional_group.add_argument("--key", dest="key", type=str, metavar="KEY", help="Key to decrypt the data (default: None)")
    
    
