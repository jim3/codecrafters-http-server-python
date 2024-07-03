Notes while I go through each exercise b/c...who can remember everything??? :)

1.  In this stage, your server will respond to an HTTP request with a 200 response.

## HTTP response

An HTTP response is made up of three parts, each separated by a CRLF (\r\n):

- Status line.
- Zero or more headers, each ending with a CRLF.
- Optional response body.

In this stage, your server's response will only contain a **status line**. Here's the response your server must send:

`HTTP/1.1 200 OK\r\n\r\n`

---

General syntax for the **socket** method, represents the address family and protocol of the transport layer

`s = socket.socket (socket_family, socket_type, protocol=0)`

---

`server_socket.accept()` | The return value is a pair (conn, address) where,

`conn` is a new socket object usable to send and receive data on the connection,
and `address` is the address bound to the socket on the other end of the connection.
server_socket.accept() # wait for client

> The return value is a pair (conn, address) where,
> `conn` is a new socket object usable to send and receive data on the connection,
> and `address` is the address bound to the socket on the other end of the connection.

```python
while True:
# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established.")

# Send HTTP response
response = b"HTTP/1.1 200 OK\r\n\r\n"
client_socket.sendall(response)

# Close the client connection
client_socket.close()
print(f"Connection from {client_address} has been closed.")
```
            
            print(f"Connection from {client_socket.getpeername()} has been closed.")   
