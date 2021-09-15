import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)


def handle_client(conn, addr):
    print("[NEW CONNECTION]", addr, "connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode("utf-8")
        if (msg_length):
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode("utf-8")
            print(addr, msg)
            if msg == "DISCONNECT":
                connected = False


def start():
    server.listen()
    print("[LISTENING] server is listening on:", SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("[ACTIVE CONNECTIONS]", str(threading.activeCount() - 1))


print("[STARTING] server is starting...")
start()
