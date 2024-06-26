import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.199"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # padd send_length to 64 byte coz server is expecting 64 length message containing msg_length
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
send("Hello World!")