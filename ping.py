import subprocess
import sys

if len(sys.argv) == 1:
    print('Вы не указали имя файла с ip адресами. Выхожу ...')
    quit()

ip_file_name = sys.argv[1]
pingable_file_name = 'pingable.txt'
unpingable_file_name = 'unpingable.txt'

try:
    with open(ip_file_name, 'r') as fip, \
            open(pingable_file_name, 'w') as fable, \
            open(unpingable_file_name, 'w') as funable:
        for ip in fip:
            ip = ip.strip()
            command = ['ping', '-c', '1', ip]
            exit_code = subprocess.call(
                    command,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    )
            if exit_code == 0:
                fable.write(ip + '\n')
                print(ip, '- OK')
            else:
                funable.write(ip + '\n')
                print(ip, '- FAIL')
except FileNotFoundError as e:
    print('warning: can\'t find file {}'.format(e.filename))
