import socket
import re

BUFF_SZ = 1024
ENC = "utf-8"
RES200 = b"HTTP/1.1 200 OK\r\n\r\n"
RES404 = b"HTTP/1.1 404 Not Found\r\n\r\n"


# f"HTTP/1.1 {status_code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}"
def response(str_result):
    response_body = f"{str_result}".encode("utf-8")
    status_line = b"HTTP/1.1 200 OK\r\n"
    content_type = b"Content-Type: text/plain\r\n"
    content_length = f"Content-Length: {len(response_body)}\r\n".encode("utf-8")
    response_headers = content_type + content_length
    response = status_line + response_headers + b"\r\n" + response_body
    return response


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


def parse_request(conn, http_request):
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
    else:
        return RES404


def handle_connection(conn, client_address):
    print(f"Connection from {client_address} has been established...")
    data = conn.recv(BUFF_SZ)
    http_request = data.decode(ENC).split("\r\n")  # bytes to list[str]
    print(f"Request from {client_address}:\n{http_request}")
    response = parse_request(conn, http_request)  # ->
    print("Return value of response: ", response)
    conn.sendall(response)


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
