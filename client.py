import socket

DIS = "disconnect"
HEADER = 64
FORMAT = "utf-8"
PORT = 5050
SERVER = "192.168.43.215"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)

client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)




send("HELLO THIS IS SOCKET TUT")
send(DIS)