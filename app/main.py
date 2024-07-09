import socket
import threading

BUFF_SZ = 1024
ENC = "utf-8"
RES200 = b"HTTP/1.1 200 OK\r\n\r\n"
RES404 = b"HTTP/1.1 404 Not Found\r\n\r\n"


def echo_string(request_line):
    parts = request_line.split()
    if len(parts) >= 2 and parts[0] == "GET" and parts[1].startswith("/echo/"):
        return parts[1][len("/echo/") :]
    return None


def get_user_agent(headers):
    for h in headers:
        if h.startswith("User-Agent:"):
            return h[len("User-Agent: ") :]
    return ""


def get_file_name(request_line):
    file = request_line.split()
    if len(file) >= 2 and file[0] == "GET" and file[1].startswith("/files/"):
        return file[1][len("/files/") :]
    return None


def parse_request(http_request):
    request_line = http_request[0]
    headers = http_request[1:-2]

    if request_line == "GET / HTTP/1.1":
        return RES200
    elif request_line.startswith("GET /echo/"):
        str_result = echo_string(request_line)
        if str_result:
            return response(str_result)
    elif request_line.startswith("GET /user-agent"):
        user_agent = get_user_agent(headers)
        return response(user_agent)
    elif request_line.startswith("GET /files/"):
        file_name = get_file_name(request_line)
        if file_name:
            return response(file_name)
    else:
        return RES404


def response(str_result):
    response_body = f"{str_result}".encode("utf-8")
    res_body_length = len(response_body)  # Integer representing byte length
    status_line = b"HTTP/1.1 200 OK\r\n"
    content_type = b"Content-Type: application/octet-stream\r\n"
    content_length = str(res_body_length).encode("utf-8")  # -> bytes
    response_headers = content_type + content_length
    response = status_line + response_headers + b"\r\n" + response_body
    print("Printing entire response: ", response)
    return response  # -> bytes


def handle_connection(client_socket, address):
    print(f"Connection from {address} has been established...")
    data = client_socket.recv(BUFF_SZ)
    http_request = data.decode(ENC).split("\r\n")  # bytes to list[str]
    print(f"Request from {address}:\n{http_request}")
    response = parse_request(http_request)  # ->
    print("Return value of response: ", response)
    client_socket.sendall(response)


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen()

    try:
        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_connection, args=(client_socket, address)
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
