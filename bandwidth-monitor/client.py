import socket
import time

def client():
    host = '127.0.0.1'
    port = 12345
    
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect((host, port))
    
    start_time = time.time()
    
    # Receive data
    total_data = b''
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        total_data += data
    
    # Measure the end time
    end_time = time.time()
    
    client_socket.close()
    
    # Calculate time taken and data size
    time_taken = end_time - start_time
    data_size = len(total_data) * 8  # Convert bytes to bits
    
    # Calculate bandwidth
    bandwidth = data_size / time_taken
    
    print(f"Time taken: {time_taken} seconds")
    print(f"Data size: {data_size / (8 * 1024 * 1024)} MB")  # Convert bits to MB
    print(f"Bandwidth: {bandwidth / (1024 * 1024)} Mbps")  # Convert bps to Mbps

if __name__ == "__main__":
    client()
