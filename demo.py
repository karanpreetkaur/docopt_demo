# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> [<arg_new>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
[<arg_new>]       Takes any value (this is a optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
""" 

from docopt import docopt
opt = docopt(__doc__)

# define main function
def main():
    # Print arguments stored in opt
    print(opt)
    print(type(opt))
    print(opt['<arg_new>'])

if __name__ == '__main__':
    main()
