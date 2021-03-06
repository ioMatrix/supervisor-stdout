from __future__ import print_function
import sys
import time
import datetime

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def main():
    while 1:
        write_stdout('READY\n') # transition from ACKNOWLEDGED to READY
        line = sys.stdin.readline()  # read header line from stdin
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len'])) # read the event payload
        write_stdout('RESULT %s\n%s'%(len(data), data)) # transition from READY to ACKNOWLEDGED

def event_handler(event, response):
    line, data = response.split('\n', 1)
    headers = dict([ x.split(':') for x in line.split() ])
    for newline in data.splitlines():
      print( '{0} [{1}] [{2}] {3}'.format( datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), headers['processname'], headers['channel'], newline) )
    time.sleep(1)
    sys.stdout.flush()
    sys.stderr.flush()

if __name__ == '__main__':
    main()
