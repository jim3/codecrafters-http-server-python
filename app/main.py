# experimental version
import socket
import re


def server_response(content, content_type="text/plain", code=200):
    return f"HTTP/1.1 {code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n{content}"


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        try:
            # Wait for an incoming connection
            conn, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established...")
            recv_data = conn.recv(1024)
            http_request = recv_data.decode("utf-8").splitlines()  #  -> list[str]

            # Extract the request path
            request_line = http_request[0]
            split_str = request_line.split(" ")

            if len(split_str) < 2:
                continue

            path = split_str[1]

            res200 = b"HTTP/1.1 200 OK\r\n\r\n"
            res404 = b"HTTP/1.1 404 Not Found\r\n\r\n"

            if path == "/":
                conn.sendall(res200)
            elif path.startswith("/echo/"):
                pattern = r"/echo/(\S+)"
                match = re.search(pattern, request_line)

                if match:
                    str_result = match.group(1)  # print(f"Match found: {str_result}")

                    # Gather all of the responses
                    response_body = f"{str_result}".encode("utf-8")
                    status_line = b"HTTP/1.1 200 OK\r\n"
                    content_type = b"Content-Type: text/plain\r\n"
                    content_length = f"Content-Length: {len(response_body)}\r\n".encode(
                        "utf-8"
                    )

                    # Create the header response
                    response_headers = content_type + content_length
                    response = status_line + response_headers + b"\r\n" + response_body

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
