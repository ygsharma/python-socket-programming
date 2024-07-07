import socket

def server():
    # Define server address and port
    host = '0.0.0.0'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print("Server listening on port", port)
    
    # Accept a connection
    conn, addr = server_socket.accept()
    print("Connection from", addr)
    
    # Send data
    data = b'x' * 10**7  # 10 MB of data
    conn.sendall(data)
    
    # Close connection
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    server()
