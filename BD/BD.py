import re
import subprocess
import sqlite3
from colorama import Fore

def open_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        data = file.read()
    return data

def ping_ip(ip_list):
    for ip in ip_list:
        command = ['ping', '-c', '1', ip]
        exit_code = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if exit_code == 0:
            print(Fore.GREEN + ip, '- OK')
            using_database(ip, 'OK')
        else:
            print(Fore.RED + ip, '- FAIL')
            using_database(ip, "FAIL")

def using_database(ip, status):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ip_list(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, ip TEXT NOT NULL, status TEXT NOT NULL, UNIQUE(id)) 
    """)
    cursor.execute("""
    INSERT INTO ip_list (ip, status)
    SELECT ?, ?
    WHERE NOT EXISTS (SELECT * FROM ip_list WHERE ip = ?)
    """, [ip, status, ip])

    conn.commit()

def main():
    text = open_file('file.txt')
    ip_list = set(re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", text))
    ping_ip(ip_list)

if __name__ == '__main__':
    main()
