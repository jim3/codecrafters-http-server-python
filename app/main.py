import os
import socket
import threading
import argparse


BUFF_SZ = 1024
ENC = "utf-8"
RES200 = b"HTTP/1.1 200 OK\r\n\r\n"
RES404 = b"HTTP/1.1 404 Not Found\r\n\r\n"


def build_response(content_type, content_length, content):
    return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}".encode(
        ENC
    )


def echo_string(request_line):
    content_type = "text/plain"
    parts = request_line.split()
    if len(parts) >= 2 and parts[0] == "GET" and parts[1].startswith("/echo/"):
        print("echo_string: ", parts[1][len("/echo/") :])  # content
        content = parts[1][len("/echo/") :]
        content_length = len(parts[1][len("/echo/") :])
        return [content_type, content_length, content]
    return None


def get_user_agent(headers):
    content_type = "text/plain"
    for h in headers:
        if h.startswith("User-Agent:"):
            content_length = len(h[len("User-Agent: ") :])
            content = h[len("User-Agent: ") :]
            return [content_type, content_length, content]
    return ""


def get_file_name(request_line):
    file = request_line.split()
    if len(file) >= 2 and file[0] == "GET" and file[1].startswith("/files/"):
        return file[1][len("/files/") :]
    return None


def read_file(file_name, directory):
    content_type = "application/octet-stream"
    file_path = os.path.join(directory, file_name)
    print(f"file_path: {file_path}")  # debugging
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            content_length = len(content)
            return [content_type, content_length, content]
    else:
        return None


def parse_request(http_request, directory):
    request_line = http_request[0]
    headers = http_request[1:-2]
    if request_line == "GET / HTTP/1.1":
        return RES200
    elif request_line.startswith("GET /echo/"):
        str_result = echo_string(request_line)
        if str_result:
            return build_response(str_result[0], str_result[1], str_result[2])
    elif request_line.startswith("GET /user-agent"):
        user_agent = get_user_agent(headers)
        return build_response(user_agent[0], user_agent[1], user_agent[2])
    elif request_line.startswith("GET /files/"):
        file_name = get_file_name(request_line)
        if file_name:
            content = read_file(file_name, directory)
            if content is not None:
                return build_response(content[0], content[1], content[2])
            else:
                return RES404
    else:
        return RES404


def handle_connection(client_socket, address, directory):
    print(f"Connection from {address} has been established...")
    data = client_socket.recv(BUFF_SZ)
    http_request = data.decode(ENC).split("\r\n")  # bytes to list[str]
    print(f"Request from {address}:\n{http_request}")
    response = parse_request(http_request, directory)  # ->
    print("Return value of response: ", response)
    client_socket.sendall(response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str)
    args = parser.parse_args()
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.listen()

    try:
        while True:
            client_socket, address = server_socket.accept()
            client_thread = threading.Thread(
                target=handle_connection, args=(client_socket, address, args.directory)
            )
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
