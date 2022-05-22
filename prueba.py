import sys
def main(argv): 
    try:      
        opts, args = getopt.getopt(argv, "hps:", 
                                                  ["help", "prn", "server="])
    except getopt.GetoptError:          
        print("Opcion no valida")
        usage()                         
        sys.exit(2)

if __name__=='__main__':
    main(sys.argv[1:])
