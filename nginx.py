"""
Nginx控制程序
"""

import os
import commands

WORK_PATH = os.getcwd()

if __name__ == '__main__':
    print(WORK_PATH)
    output = os.popen('java -version')
    print(output.read())
    print("---------------------------------------")
    (status, output) = commands.getstatusoutput('java -version')
    print(status, output)
