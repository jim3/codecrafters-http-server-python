# experimental version
import socket
import re

BUFF_SZ = 1024
ENC = "utf-8"


def handle_connection(conn, client_address):
    print(f"Connection from {client_address} has been established...")
    data = conn.recv(BUFF_SZ)
    request = data.decode(ENC)
    print(f"Request from {client_address}:\n{request}")
    # http_method, path, user_agent, body = parse_request(request)

    # call parse_request
    response = parse_request(request)

    conn.sendall(response().encode(ENC))
    conn.close()
    # PARSE THE REQUEST
    # response = parse_request(conn, http_request)

    # SEND RESPONSE TO main FUNCTION
    # send_response_back(responose)


def parse_request(conn, http_request):
    res200 = b"HTTP/1.1 200 OK\r\n\r\n"
    res404 = b"HTTP/1.1 404 Not Found\r\n\r\n"

    # request_line = http_request[0]  # get 1st element
    # split_str = request_line.split(" ")
    # path = split_str[1]  # use split to get `/` root path

    if path == "/":
        request_line = http_request[0]  # get 1st element
        split_str = request_line.split(" ")
        path = split_str[1]  # use split to get `/` root path
        conn.sendall(res200)
    elif path.startswith("/echo/"):
        pattern = r"/echo/(\S+)"
        match = re.search(pattern, path)
        if match:
            str_result = match.group(1)  # print(f"Match found: {str_result}")
            return str_result
        else:
            conn.sendall(res404)
        conn.close()


def response(str_result):
    # Gather all of the responses
    response_body = f"{str_result}".encode("utf-8")
    status_line = b"HTTP/1.1 200 OK\r\n"
    content_type = b"Content-Type: text/plain\r\n"
    content_length = f"Content-Length: {len(response_body)}\r\n".encode("utf-8")

    # Create the header response
    response_headers = content_type + content_length
    response = status_line + response_headers + b"\r\n" + response_body

    # return response
    return response


def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        conn, client_address = server_socket.accept()
        handle_connection(conn, client_address)


if __name__ == "__main__":
    main()
