import sys;

def argsTest(*args):
    list_input = list(args[0]) # this returns a list argument of  the input from the program
    for arg in list_input:
        print(arg)


if __name__ == '__main__':
    argsTest(sys.argv[1:])