### Socket module

```bash
`(module) socket`

This module provides socket operations and some related functions. On Unix, it supports IP (Internet Protocol) and Unix domain sockets. On other systems, it only supports IP. Functions specific for a socket are available as methods of the socket object.

Functions:

- socket() -- create a new socket object 
- socketpair() -- create a pair of new socket objects [*] 
- fromfd() -- create a socket object from an open file descriptor [*] send_fds() -- Send file descriptor to the socket. recv_fds() -- Receive file descriptors from the socket. fromshare() -- create a socket object from data received from socket.share() [*] gethostname() -- return the current hostname gethostbyname() -- map a hostname to its IP number gethostbyaddr() -- map an IP number or hostname to DNS info getservbyname() -- map a service name and a protocol name to a port number getprotobyname() -- map a protocol name (e.g. 'tcp') to a number ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order htons(), htonl() -- convert 16, 32 bit int from host to network byte order inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89) socket.getdefaulttimeout() -- get the default timeout value socket.setdefaulttimeout() -- set the default timeout value create_connection() -- connects to an address, with an optional timeout and
                       optional source address.
create_server() -- create a TCP socket and bind it to a specified address.

 [*] not available on all platforms!
```

---

```py
for i in range(len(request_line)):
    print(request_line[i])
printing http_request[0] GET /banana HTTP/1.1
[your_program] split on whitespace:  ['GET', '/banana', 'HTTP/1.1']""
```

```bash
[your_program] printing http_request[0] GET /orange HTTP/1.1
[your_program] split on whitespace:  ['GET', '/orange', 'HTTP/1.1']
[your_program] /orange
```

```bash
tester::#IH0] Running tests for Stage #IH0 (Extract URL path)
[tester::#IH0] Running program
[tester::#IH0] $ ./your_server.sh
[your_program] Logs from your program will appear here!
[tester::#IH0] Connected to localhost port 4221
[tester::#IH0] $ curl -v http://localhost:4221/banana
[tester::#IH0] > GET /banana HTTP/1.1
[tester::#IH0] > Host: localhost:4221
[tester::#IH0] >
[tester::#IH0] Sent bytes: "GET /bananaimport socket

def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        try:
            # Accept a connection
            conn, client_address = server_socket.accept()
            print(f"Connection from {client_address} has been established.")

            # Send HTTP response to the client using `sendall()`
            response = b"HTTP/1.1 200 OK\r\n\r\n"
            response_404 = b"HTTP/1.1 404 Not Found\r\n\r\n"
            # conn.sendall(response)

            # get the http request
            recv_data = conn.recv(1024) # /socket.html#socket.socket.recv

            # Decode the [bytes]/request returns `list[str]`
            http_request = recv_data.decode('utf-8').splitlines()
            request_line = http_request[0]

            for v in request_line:
                print("split on whitespace: ", request_line.split(' '))
                split_str = request_line.split(' ')
                print(split_str[1])
                if(split_str[1] != '/'):
                    conn.sendall(response_404)
                elif(split_str[1]=='/'):
                    conn.sendall(response)
                else:
                    "error!"

        finally:
            # Close the client connection regardless of exceptions
            conn.close()
            print(f"Connection from {client_address} has been closed.")


if __name__ == "__main__":
    main()

[your_program] request_line
[your_program] request_line /
[your_program] request_line b
[your_program] request_line a
[tester::#IH0] Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#IH0] < HTTP/1.1 200 OK
[tester::#IH0] <
[your_program] request_line n
[your_program] request_line a
[your_program] request_line n
[your_program] request_line a
[your_program] request_line
[tester::#IH0] Expected status code 404, got 200
[tester::#IH0] Test failed
[tester::#IH0] Terminating program
[your_program] request_line H
[your_program] request_line T
[your_program] request_line T
[your_program] request_line P
[your_program] request_line /
[your_program] request_line 1
[your_program] request_line .
[your_program] request_line 1
[your_program] Connection from ('127.0.0.1', 51014) has been closed.
[tester::#IH0] Program terminated successfully
```

---

```bash
[tester::#IH0] Sent bytes: "GET /orange HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 56698) has been established.
[your_program] printing http_request[0] GET /orange HTTP/1.1
[your_program] http_request GET /orange HTTP/1.1 # http_request[0]
[your_program] http_request Host: localhost:4221 # http_request[1]
[your_program] http_request
```

```bash
[tester::#IH0] Running tests for Stage #IH0 (Extract URL path)
[tester::#IH0] Running program
[tester::#IH0] $ ./your_server.sh
[your_program] Logs from your program will appear here!
[tester::#IH0] Connected to localhost port 4221
[tester::#IH0] $ curl -v http://localhost:4221/orange
[tester::#IH0] > GET /orange HTTP/1.1
[tester::#IH0] > Host: localhost:4221
[tester::#IH0] >
[tester::#IH0] Sent bytes: "GET /orange HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 56698) has been established.
[your_program] printing http_request[1] GET /orange HTTP/1.1
[your_program] http_request GET /orange HTTP/1.1
[your_program] http_request Host: localhost:4221
[your_program] http_request
[your_program] Connection from ('127.0.0.1', 56698) has been closed.
[tester::#IH0] Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#IH0] < HTTP/1.1 200 OK
[tester::#IH0] <
[tester::#IH0] Expected status code 404, got 200
[tester::#IH0] Test failed
[tester::#IH0] Terminating program
[tester::#IH0] Program terminated successfully

```

**Note:** To try this locally, you could run `./your_server.sh` in one terminal session,
and `nc -vz 127.0.0.1 4221` in another. (`-v` gives more verbose output, `-z` just scans for listening daemons, without sending any data to them.)

Notes while I go through each exercise b/c...who can remember everything???...

# Step 1 | Response with 200

1.  In this stage, your server will respond to an HTTP request with a 200 response.

## HTTP response

An HTTP response is made up of three parts, each separated by a CRLF (\r\n):

- Status line.
- Zero or more headers, each ending with a CRLF.
- Optional response body.

In this stage, your server's response will only contain a **status line**. Here's the response your server must send: `HTTP/1.1 200 OK\r\n\r\n`

General syntax for the **socket** method, represents the address family and protocol of the transport layer

- `s = socket.socket (socket_family, socket_type, protocol=0)`

- `server_socket.accept()` | The return value is a pair `(conn, address)` where,

- `conn` is a new socket object usable to send and receive data on the connection,
  and `address` is the address bound to the socket on the other end of the connection.

- The return value is a object pair `(conn, address)` where..
- `conn` is a new socket object usable _to send and receive data_ on the connection,
- and `address` is the address bound to the socket on the other end of the connection.

---

# Step 2 - Extract URL path

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages#request_line

In this stage, your server will extract the URL path from an HTTP request, and respond with either a 200 or 404, depending on the path.

**HTTP request**

An HTTP request is made up of _three parts_, each separated by a CRLF (`\r\n`):

- Request line
- Zero or more headers, each ending with a CRLF
- Optional request body

Here's an example of an HTTP request:

`GET /index.html HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: curl/7.64.1\r\nAccept: */*\r\n\r\n`

Here is a breakdown of the request:

```c
// Request line
GET                          // HTTP method
/index.html                  // Request target
HTTP/1.1                     // HTTP version
\r\n                         // CRLF that marks the end of the request line

// Headers
Host: localhost:4221\r\n     // Header that specifies the server's host and port
User-Agent: curl/7.64.1\r\n  // Header that describes the client's user agent
Accept: */*\r\n              // Header that specifies which media types the client can accept
\r\n                         // CRLF that marks the end of the headers

// Request body (empty)
```

The "request target" specifies the URL path for this request. In this example, the URL path is `/index.html`

Note that each header ends in a **CRLF**, and the entire header section also ends in a **CRLF**.

---

# Step 3 - Respond with body

---
