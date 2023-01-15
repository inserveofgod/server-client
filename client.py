import socket
import time

# create socket here
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# set the hostname and define default port
host = "127.0.1.1"
port = 1919
encoding = "UTF-8"


try:
    # Try to connect to the server
    print(f"[*] {time.ctime(time.time())} --- Connecting on {port} with ip {host} ...")
    s.connect((host, port))
    print(f"[+] {time.ctime(time.time())} --- Connected.")

    # wait until user sends 'q' keystroke
    while True:
        # get data from the visitor
        data = s.recv(1024).decode(encoding)
        print(f"{time.ctime(time.time())} --- Message: ", data)

        msg = input("Send : ")
        s.send(msg.encode(encoding))

        # send data to visitor
        if msg == 'q':
            print(f"{time.ctime(time.time())} --- Good bye!")
            s.close()
            break

except ConnectionRefusedError:
    print(f"[!] {time.ctime(time.time())} --- Could not connected!")

except BrokenPipeError:
    print(f"[!] {time.ctime(time.time())} --- Connection is terminated by the server!")
