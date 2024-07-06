import socket
import re

BUFF_SZ = 1024
ENC = "utf-8"


def handle_connection(conn, client_address):
    print(f"Connection from {client_address} has been established...")
    data = conn.recv(BUFF_SZ)
    # http_request = data.decode(ENC)
    http_request: list[str] = data.decode(ENC).splitlines()  # Specify type as list[str]
    print(f"Request from {client_address}:\n{http_request}")

    # call parse_request
    response = parse_request(conn, http_request)
    print("value of response variable ->", response)
    # conn.sendall(response().encode(ENC))
    conn.close()

    # SEND RESPONSE TO main FUNCTION
    # send_response_back(responose)


def parse_request(conn, http_request):
    print("Value of http_request: ", http_request)
    # ['GET /user-agent HTTP/1.1', 'Host: localhost:4221', 'User-Agent: orange/grape-orange', '']

    res200 = b"HTTP/1.1 200 OK\r\n\r\n"
    res404 = b"HTTP/1.1 404 Not Found\r\n\r\n"

    request_line = http_request[0]  # get 1st element
    print("request_line value: ", request_line)

    split_str = request_line.split(" ")
    print("split_str: ", split_str)
    path = split_str[1]  # use split to get `/` root path

    if path == "/":
        conn.sendall(res200)
    elif path.startswith("/echo/"):
        pattern = r"/echo/(\S+)"
        match = re.search(pattern, path)
        if match:
            str_result = match.group(1)  # print(f"Match found: {str_result}")
            return str_result
    elif path.startswith("/user-agent"):
        print("we got user-agent!!!!")

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
    print("Server is listening on port 4221...")

    while True:
        conn, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established.")
        handle_connection(conn, client_address)
        conn.close()


if __name__ == "__main__":
    main()
