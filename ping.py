import subprocess

ip_file_name = 'iplist.txt'
pingable_file_name = 'pingable.txt'
unpingable_file_name = 'unpingable.txt'

try:
    with open(ip_file_name, 'r') as fip, \
            open(pingable_file_name, 'w') as fable, \
            open(unpingable_file_name, 'w') as funable:
        for ip in fip:
            ip = ip.strip()
            command = ['ping', '-c', '1', ip]
            exit_code = subprocess.call(command)
            if exit_code == 0:
                fable.write(ip + '\n')
            else:
                funable.write(ip + '\n')
except FileNotFoundError as e:
    print('warning: can\'t find file {}'.format(e.filename))
