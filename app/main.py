# experimental version
import socket
import re


def handle_connection(conn, client_address):
    print(f"Connection from {client_address} has been established...")
    try:
        recv_data = conn.recv(1024)
        http_request = recv_data.decode("utf-8").splitlines()
        print(f"Request from {client_address}:\n{http_request}")

        # PARSE THE REQUEST
        response = parse_request(conn, http_request)

        # SEND RESPONSE TO main FUNCTION
        # [*]

    except UnicodeDecodeError:
        print(f"Error decoding data from client {client_address}")
    finally:
        conn.close()
        print(f"Connection from {client_address} has been closed.")


def parse_request(conn, http_request):
    res200 = b"HTTP/1.1 200 OK\r\n\r\n"
    res404 = b"HTTP/1.1 404 Not Found\r\n\r\n"

    # Extract path from http_request[] ['GET / HTTP/1.1', [1], [2]]
    request_line = http_request[0]  # 'GET / HTTP/1.1'
    split_str = request_line.split(" ")

    # Extract the path
    path = split_str[1]  # `/` [`/echo/{str}/` | `/user-agent/`]

    if path == "/":
        conn.sendall(res200)
    elif path.startswith("/echo/"):
        pattern = r"/echo/(\S+)"
        match = re.search(pattern, path)

        if match:
            str_result = match.group(1)  # print(f"Match found: {str_result}")

            # Gather all of the responses
            response_body = f"{str_result}".encode("utf-8")
            status_line = b"HTTP/1.1 200 OK\r\n"
            content_type = b"Content-Type: text/plain\r\n"
            content_length = f"Content-Length: {len(response_body)}\r\n".encode("utf-8")

            # Create the header response
            response_headers = content_type + content_length
            response = status_line + response_headers + b"\r\n" + response_body
            # return f"HTTP/1.1 {code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(content)}\r\n\r\n{content}"

            # return response
            return response
        else:
            conn.sendall(res404)
        conn.close()


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        conn, client_address = server_socket.accept()
        handle_connection(conn, client_address)


if __name__ == "__main__":
    main()
