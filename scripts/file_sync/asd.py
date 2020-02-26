import socket
import os
import sys

if sys.argv[1] == 'get':
    directory_list = []
    hostname = socket.gethostname()
    for root, subFolder, files in os.walk("/home/" + hostname):
        for name in files:
            directory_list.append(' '.join(os.path.join(root, name).split("/")[:-2]).replace(' ', '/'))

    with open(hostname+'-output.txt', 'w') as file_out:
        for item in directory_list:
            file_out.write("%s\n" % item)
