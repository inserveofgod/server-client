import socket
import time

# create socket here
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# get the host by hostname and define default port
host = socket.gethostbyname(socket.gethostname())
port = 1919
encoding = "UTF-8"

# listen for connections
s.bind((host, port))
s.listen(5)

while True:
    # accept the connection if someone tries to connect
    print(f"[*] {time.ctime(time.time())} --- Listening on {port} with ip {host} ...")
    visitor, visitor_addr = s.accept()

    # send welcome message to visitor
    print(f"[+] {time.ctime(time.time())} --- Visitor connected on {visitor_addr[1]} with ip {visitor_addr[0]}.")
    visitor.send("Welcome".encode(encoding))

    # wait until user sends 'q' keystroke
    while True:
        # get data from the visitor
        data = visitor.recv(1024).decode(encoding)
        print(f"{time.ctime(time.time())} --- Message: ", data)

        if data == 'q':
            print(f"{time.ctime(time.time())} --- Good bye!")
            visitor.close()
            break

        # send data to visitor
        msg = input("Send : ")
        visitor.send(msg.encode(encoding))
