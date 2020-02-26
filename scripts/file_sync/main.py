import socket, sys, os
import multiprocessing


def get_error():
    print("Example Usage: python " + sys.argv[0] + " compare ank-psl.txt ist-psl.txt")
    print("Example Usage: python " + sys.argv[0] + " get outputfile.txt")
    os._exit(2)

def file_sync():

    if len(sys.argv) < 1:
        get_error()

    if sys.argv[1] == 'get':
        outputfile = sys.argv[2]
        directory_list = []
        hostname = socket.gethostname()
        for root, subFolder, files in os.walk("/home/" + hostname):
            for name in files:
                directory_list.append(' '.join(os.path.join(root, name).split("/")[:-2]).replace(' ', '/'))

        with open(outputfile, 'w') as file_out:
            for item in directory_list:
                file_out.write("%s\n" % item)

    elif sys.argv[1] == 'compare':
        filename1 = sys.argv[2]
        filename2 = sys.argv[3]

        file_list = []
        liste = []
        liste3 = []
        jobs = []


        with open('/tmp/asd/test1', 'r') as file1:
            for line1 in file1:
                line1 = line1.split(" ")[0]
                liste.append(line1)
        with open('/tmp/asd/test2', 'r') as file2:
            for line2 in file2:
                line2 = line2.split(" ")[0]
                if line2 not in liste:
                    liste3.append(line2)

        with open('some_output_file.txt', 'w') as file_out:
            for item in liste3:
                file_out.write("%s\n" % item)
    else:
        get_error()


if __name__=="__main__":
    try:
        file_sync()
    except IndexError:
        print "You did not specify a file"
        sys.exit(1)