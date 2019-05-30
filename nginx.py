"""
Nginx控制程序
"""

import os
import subprocess

# import paramiko
# import time
# import commands

WORK_PATH = os.getcwd()
# ssh = paramiko.SSHClient()
# sc = ssh.invoke_shell()
# root_pwd = 'nikai'


# def exe_cmd(cmd, t=0.1):
#     sc.send(cmd)
#     sc.send("\n")
#     time.sleep(t)
#     resp = sc.recv(9999).decode("utf8")
#     print "cmd='%s',echo='%s'\n"%(cmd,resp)
#     return resp


if __name__ == '__main__':
    print(WORK_PATH)
    output = os.popen('nginx -t')
    output_read = output.read()
    # result = str(output_read)
    # print(output_read)
    # print(result)

    # print(output_read)
    print("==========================")
    # validation = output_read.split(' ')[-1]
    # print(validation)
    output = os.popen('nginx -s reload')
    # print(output.read())
    print("---------------------------------------")
    # (status, output) = commands.getstatusoutput('java -version')
    # print(status, output)
    # 切换root账号
    # resp = exe_cmd("su root", t=100)
    # if resp.endswith(u"密码："):
    #     resp = exe_cmd(root_pwd)
