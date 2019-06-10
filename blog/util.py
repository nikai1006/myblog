import os


def cout_user(dest):
    if os.path.exists(dest) and os.path.isdir(dest):
        ip_dict = {}
        logs = os.listdir(dest)
        for log in logs:
            dest_log = dest + "/" + log
            if os.path.isfile(dest_log):
                for line in open(file=dest_log, mode='r', encoding='UTF-8'):
                    if ' session exceptionCaught ' in line and '123.58.32.72:6922) (ServerHandler.exceptionCaught(101))' in line:
                        host = get_remote_host(line)
                        if host not in ip_dict:
                            ip_dict[host] = 1
                        else:
                            ip_dict[host] += 1
        result_list = sorted(ip_dict.items(), key=lambda t: t[1], reverse=True)
        for ip, num in result_list:
            print("ip", ip, '出现 %d 次' % num)
        return result_list


def get_remote_host(line):
    word = str(line).split('/')[1]
    return word.split(':')[0]


if __name__ == '__main__':
    cout_user("C:\\Users\oeasy\Desktop\split.log")
