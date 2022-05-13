import subprocess
import time
import random

def getFile(url):
    a=subprocess.Popen(["./dezoomify-rs"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    input = "{0}\n".format(url)
    a.stdin.write(str.encode(input))
    a.stdin.write(b"0\n")
    a.stdin.close()

    out = a.stdout.read()
    a.stdout.close()
    #print(out)
    rst = str(out,encoding='utf-8').split("\n")
    print(rst[len(rst)-4]);
    print(rst[len(rst)-2]);

if __name__ == '__main__':
    filename = './url.txt'
    count = 0
    with open(filename, 'r', encoding='UTF-8') as file:
        line = file.readline()
        while line is not None and line != '':
            print('url: '+ line)
            getFile(line)
            #break;
            line = file.readline()
            time.sleep(random.randint(0,30))
