import getopt, sys, os

def main(argv):
    try:
        opt, args = getopt.getopt(argv, "he:da:", ["help", "execute=", "dothis", "argument="])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opt:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", "--execute"):
            os.system(a)
        elif o in ("-d", "--dothis"):
            print "dothis"
        elif o in ("-a", "--argument"):
            print str(a)
        else:
            assert False, "unhandled option"
def usage():
    usage = """
    -h --help                 Prints this
    -e --execute (cmd)        Execute a system command
    -d --dothis               Print dothis
    -a --argument (argument   Print (argument)
    """
    print usage

if __name__ == "__main__":
    main(sys.argv[1:]) # [1:] slices off the first argument which is the name of the program

