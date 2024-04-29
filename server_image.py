import socket
from PIL import Image
import time

def receive_file(connection, filename):
    file_length = int(connection.recv(1024).decode())
    connection.send(b'LENGTH RECEIVED')

    with open(filename, 'wb') as file_to_write:
        bytes_received = 0
        while bytes_received < file_length:
            data = connection.recv(1024)
            if not data:
                break
            file_to_write.write(data)
            bytes_received += len(data)

def start_server(host, port, filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print("Server listening...")

        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        receive_file(client_socket, filename)
        print(f"File {filename} has been received.")
        
        # Display the received image
        img = Image.open(filename)
        #print(img.size)
        #img = img.transpose(Image.TRANSPOSE)
        print(img.size)
        print('with 80% loss')
        with open('/home/wifi/Desktop/codes/received_image_80.jpg', 'wb') as file_:
        	img.save(file_)


if __name__ == "__main__":
    HOST = '0.0.0.0'
    PORT = 12345
    FILENAME = "received_image.jpg"
    start_server(HOST, PORT, FILENAME)
