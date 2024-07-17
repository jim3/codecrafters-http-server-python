import os
import socket
import threading
import argparse


BUFF_SZ = 1024
ENC = "utf-8"
RES200 = b"HTTP/1.1 200 OK\r\n\r\n"
RES201 = b"HTTP/1.1 201 Created\r\n\r\n"
RES404 = b"HTTP/1.1 404 Not Found\r\n\r\n"


def build_response(status_code, content_type, content_length, content, encoding=None):
    response = f"HTTP/1.1 {status_code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n"
    if encoding:
        response += f"{encoding}\r\n"
    response += f"\r\n{content}"
    return response.encode(ENC)


def echo_string(request_line):
    status_code = 200
    content_type = "text/plain"
    parts = request_line.split()
    if len(parts) >= 2 and parts[0] == "GET" and parts[1].startswith("/echo/"):
        content = parts[1][len("/echo/") :]
        content_length = len(parts[1][len("/echo/") :])
        return [status_code, content_type, content_length, content]
    return None


def get_user_agent(headers):
    status_code = 200
    content_type = "text/plain"
    for h in headers:
        if h.startswith("User-Agent:"):
            content_length = len(h[len("User-Agent: ") :])
            content = h[len("User-Agent: ") :]
            return [status_code, content_type, content_length, content]
    return ""


def get_file_name(request_line):
    file = request_line.split()
    if len(file) >= 2 and file[0] == "GET" and file[1].startswith("/files/"):
        return file[1][len("/files/") :]
    elif len(file) >= 2 and file[0] == "POST" and file[1].startswith("/files/"):
        return file[1][len("/files/") :]
    return None


def read_file(file_name, directory):
    status_code = str(200)
    content_type = "application/octet-stream"
    file_path = os.path.join(directory, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            content_length = len(content)
            return [status_code, content_type, content_length, content]
    else:
        return None


def create_file(file_name, directory, rbody):
    code = "201 Created\r\n\r\n"
    status_code = str(code)
    content_type = "application/octet-stream"
    req_body = rbody[0]
    file_path = os.path.join(directory, file_name)
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(req_body)
            content_length = len(req_body)
            return [status_code, content_type, content_length, req_body]
    else:
        return None


def content_encoding(headers):
    heading = "Content-Encoding: "
    gzip = "gzip"
    if any("Accept-Encoding: invalid-encoding" in h for h in headers):
        return None
    else:
        for h in headers:
            if h.startswith("Accept-Encoding:"):
                return f"{heading}{gzip}"
        return None


def parse_request(http_request, directory):
    print(f"HTTP Request: {http_request}")
    request_line = http_request[0]
    print(f"HTTP Request line: {request_line}")
    headers = http_request[1:-2]
    print(f"HTTP Request headers: {headers}")

    user_agent = get_user_agent(headers)
    encoding = content_encoding(headers)
    print(f"HTTP Request encoding: {encoding}")
    rbody = http_request[-1:]
    print(f"HTTP Request body: {rbody}")

    # GET /
    if request_line == "GET / HTTP/1.1":
        return RES200
    # GET /echo/{str}
    elif request_line.startswith("GET /echo"):
        str_result = echo_string(request_line)
        if str_result:
            str_result.append(encoding)
            print("str_result after append: ", str_result)
            return build_response(
                str_result[0],
                str_result[1],
                str_result[2],
                str_result[3],
                str_result[4],
            )
    # GET /user-agent
    elif request_line.startswith("GET /user-agent"):
        user_agent = get_user_agent(headers)
        return build_response(
            user_agent[0], user_agent[1], user_agent[2], user_agent[3]
        )
    # GET /files/{filename}
    elif request_line.startswith("GET /files"):
        file_name = get_file_name(request_line)
        if file_name:
            content = read_file(file_name, directory)
            if content is not None:
                return build_response(content[0], content[1], content[2], content[3])
            else:
                return RES404
    # POST /files/{filename}
    elif request_line.startswith("POST /files"):
        file_name = get_file_name(request_line)  # ->
        print("file_name to create: ", file_name)
        if file_name:
            req_body = create_file(file_name, directory, rbody)
            if req_body:
                return build_response(
                    req_body[0], req_body[1], req_body[2], req_body[3]
                )
            else:
                return RES404
    else:
        return RES404


def handle_connection(client_socket, address, directory):
    print(f"Connection from {address} has been established...")
    data = client_socket.recv(BUFF_SZ)
    print(f"Raw request: {data}")
    http_request = data.decode(ENC).split("\r\n")
    response = parse_request(http_request, directory)
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
