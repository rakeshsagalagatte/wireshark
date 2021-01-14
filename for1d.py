import sys
import subprocess

def n_MSG_request(filename,MSG):
    fields = 'http.request.method == ' + MSG
    command = str('tshark -r ' + filename + ' -Y -T fields -e http.request.method').split()
    command.insert(4, fields)
    n_packet = subprocess.Popen(command , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = n_packet.communicate()
    stdout = str(stdout.decode('utf-8').replace('\n', ' ')).split()
    print('There are ' + str(len(stdout)) + ' HTTP ' + MSG + ' request  messages  did  our  browser  send.')
    return


def main():
    if len(sys.argv) != 3:
        er = '''Syntax ERROR:
                Use like : python3 for1cde.py filename.pcapng HTTP_METHOD.
                exit code 1.'''
        print(er)
        exit(1)
    filename = sys.argv[1]
    MSG = sys.argv[2]
    n_MSG_request(filename, MSG)

if __name__=='__main__':
    main()