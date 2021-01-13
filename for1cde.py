import pyshark
import sys
import subprocess

def n_MSG_request(filename, MSG):
    fields = 'http.request.method == ' + MSG
    command = str('tshark -r ' + filename + ' -Y -T fields -e http.request.method -e ipv6.flow').split()
    command.insert(4, fields)
    try:
        n_packet = subprocess.Popen(command , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except :
        command = str('tshark -r ' + filename + ' -Y -T fields -e http.request.method -e ip.id').split()
        command.insert(4, fields)
        n_packet = subprocess.Popen(command , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = n_packet.communicate()
    stdout = str(stdout.decode('utf-8').replace('\n', ' ')).split()
    print('There are ' + str(int(len(stdout)/2)) + ' ' + MSG + ' packets ')
    if int(len(stdout)/2) == 0:
        return
    print('Packet ID and HTTP MSG')
    for i in range(0,len(stdout),2):
        print(stdout[i+1] + '\t' + stdout[i])


def main():
    if len(sys.argv) != 3:
        er = '''Syntax ERROR:
                Use like : python3 for1cde.py filename.pcapng HTTP_MSG.
                exit code 1.'''
        print(er)
        exit(1)
    filename = sys.argv[1]
    MSG = sys.argv[2]
    n_MSG_request(filename, MSG)

if __name__=='__main__':
    main()