import subprocess
import sys

# gaia.cs.umass ip == 128.119.245.12

def response_gaia(filename):
    command = str('tshark -r ' + filename + ' -Y  -T fields -e http.response.code -e http.response.phrase').split()
    protocol = "ip.host==128.119.245.12 and http.response"
    command.insert(4,protocol)
    n_packet = subprocess.Popen(command , stdout=subprocess.PIPE , stderr=subprocess.STDOUT)
    stdout,stderr = n_packet.communicate()
    stdout = str(stdout.decode('utf-8')).split('\n')
    print('Status code and phrase')
    for i in stdout:
        print(i)
    print('When the HTTP GET message for the second time, http.authbasic was the new field is included in the HTTP GET message. Which is for authentication.')

def main():
    if len(sys.argv) != 2:
        er = '''Syntax ERROR:
                Use like : python3 for1cde.py filename.pcapng.
                exit code 1.'''
        print(er)
        exit(1)
    filename = sys.argv[1]
    # MSG = sys.argv[2]
    response_gaia(filename)

if __name__=='__main__':
    main()