import socket


def client_program():
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host,port))
    number = str(input("Enter number: "))
    while int(number) is not 00:
        client_socket.send(number.encode())
        data = client_socket.recv(1024).decode()
        print (data)
        number = str(input("Enter number: "))
    client_socket.close()


if __name__ == '__main__':
    client_program()