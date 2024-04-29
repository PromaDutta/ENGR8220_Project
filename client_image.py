import socket
import os

def send_file(host, port, filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        file_size = os.path.getsize(filename)
        client_socket.send(str(file_size).encode())
        client_socket.recv(1024)  # Wait for the server to acknowledge

        with open(filename, 'rb') as file_to_send:
            for data in file_to_send:
                client_socket.sendall(data)
        print("File has been sent.")
        
if __name__ == "__main__":
    HOST = '0.0.0.0'  # Replace with the server's actual IP address
    PORT = 12345
    FILENAME = "/home/wifi/Desktop/codes/pothole2.jpg"  # Replace with the path to your image file
    send_file(HOST, PORT, FILENAME)
