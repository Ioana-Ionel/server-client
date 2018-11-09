import socket
# from __future__ import print_function


def prime_numbers(a):
    if a is 0 or a is 1:
        return False
    for d in range(2, a/2):
        if a % d == 0:
            return False
    return True


def server_program():
    host = socket.gethostname()
    port = 5000
    # initiate connection
    server_socket=socket.socket()
    # bind host address and port together
    server_socket.bind((host, port))
    # set how many clients the server can have at the same time
    server_socket.listen(3)
    conn, address = server_socket.accept()
    print ('Connection from ', str(address))
    while True:
        # the data received from the client
        data = conn.recv(1025).decode()
        if not data:
            break
        print ('from connected user: ' + str(data))
        data = int(data)
        print('the number is ' + str(data) + '. Is it prime?  ' + str(prime_numbers(data)))
        if prime_numbers(data) is True:
            data = 'The number is prime'
        else:
            data = 'The number is not prime'
        # send data to the client
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()