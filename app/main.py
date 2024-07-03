# Uncomment this to pass the first stage
import socket


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    # server_socket.accept() # wait for client
    while True:
        try:
            # Accept a connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established.")

            # Send HTTP response to the client
            response = b"HTTP/1.1 200 OK\r\n\r\n"
            client_socket.sendall(response)
        finally:
            # Close the client connection regardless of exceptions
            client_socket.close()
            print(f"Connection from {client_address} has been closed.")

# --------------------------------------------- #

if __name__ == "__main__":
    main()
