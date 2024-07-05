import socket
import re

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    while True:
        try:
            conn, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established...")
            # receive data from the socket. return value is a bytes object
            recv_data = conn.recv(1024)
            http_request = recv_data.decode('utf-8').splitlines() # -> list[str]

            # Extract the request path
            request_line = http_request[0]
            split_str = request_line.split(' ')

            if len(split_str) < 2:
                continue

            path= split_str[1]

            res200 = b"HTTP/1.1 200 OK\r\n\r\n"
            res404 = b"HTTP/1.1 404 Not Found\r\n\r\n"

            if path == '/':
                conn.sendall(res200)
            elif path.startswith('/echo/'):
                pattern = r"/echo/(\S+)"
                match = re.search(pattern, request_line)

                if match:
                    str_result = match.group(1) # print(f"Match found: {str_result}")
                    
                    # Gather all of our responses
                    response_body = f"{str_result}".encode('utf-8') # Encode response_body to utf-8 bytes
                    status_line = b"HTTP/1.1 200 OK\r\n"
                    content_type = b"Content-Type: text/plain\r\n"
                    content_length = f"Content-Length: {len(response_body)}\r\n".encode('utf-8')
                    response_headers = (content_type + content_length) # Create the header response
                    response = status_line + response_headers + b"\r\n" + response_body # Create the response

                    # send the response back to the client
                    conn.sendall(response)
                else:
                    conn.sendall(res404)
            else:
                conn.sendall(res404)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
            print(f"Connection from {client_address} has been closed.")

if __name__ == "__main__":
    main()
