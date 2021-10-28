import os
import signal
from subprocess import Popen, PIPE

def terminate_port(port):
    process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:       
        data = [x for x in process.split(" ") if x != '']
        if (len(data) <= 1):
            continue
        os.kill(int(data[1]), signal.SIGKILL)

def store_cookie(address):
    try:
        f =  open("cookies.txt", "r+")
        line = 'a'
        flag = 1
        while line != '':
            line = f.readline()
            if line.strip("\n") == str(address):
                print('Cookie present.')
                next_line_count = f.readline()
                f.seek(f.tell() - len(next_line_count))
                f.write(str(int(next_line_count) + 1))  # increment
                flag = 0
                break
        if flag:        # if client requests for first time
            f.write(str(address) + '\n')
            f.write('1\n')
        f.close()
    except Exception as e:
        print(e)

 # for line in lines:
        #     if line.find("Host: ") != -1:
        #         host = line[6 :]
        #         print(host)
        #     if line.find("User-Agent: ") != -1:
        #         user = line[12:]
        #         print(user)
        #     if line.find('Accept: ') != -1:
        #         acpt = line[8 :]
        #         print(acpt)
        #     if line.find('Accept-Encoding: ') != -1:
        #         acpt_enco = line[17 :]
        #         print(acpt_enco)