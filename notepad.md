`HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 14\r\n\r\nHello, World!`
`HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}`
`return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}"`

> Example of response for read file stage:

```py
res = "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 57\r\n\r\npineapple raspberry mango orange orange mango apple grape"
return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}"
```

```bash
[tester::#FS3] Sent bytes: "GET /user-agent HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: strawberry/pear-strawberry\r\n\r\n"
[your_program] Return value of response: b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: t\r\n\r\ns'
[tester::#FS3] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: t\r\n\r\n"
```

```py
file_content = [content_type, content_length, content]
content_type = content[0],
content_length = content[1],
content = content[2]

response = f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}"

# or

response = f"HTTP/1.1 200 OK\r\nContent-Type: {file_content[0]}\r\nContent-Length: {file_content[1]}\r\n\r\n{file_content[2]}"

```

```bash
jim3@jim3-9020:~/.../codecrafters-http-server-python$ codecrafters test
Initiating test run...

⚡ This is a turbo test run. https://codecrafters.io/turbo

Running tests. Logs should appear shortly...

[compile] Compilation successful.

Debug = true

# [tester::#AP6] Running tests for Stage #AP6 (Return a file)
[tester::#AP6] Running program
[tester::#AP6] $ ./your_server.sh --directory /tmp/data/codecrafters.io/http-server-tester/
[tester::#AP6] Testing existing file
[tester::#AP6] Creating file banana_mango_blueberry_orange in /tmp/data/codecrafters.io/http-server-tester/
[tester::#AP6] File Content: "pineapple raspberry mango orange orange mango apple grape"
[tester::#AP6] Connected to localhost port 4221
[tester::#AP6] $ curl -v http://localhost:4221/files/banana_mango_blueberry_orange
[tester::#AP6] > GET /files/banana_mango_blueberry_orange HTTP/1.1
[tester::#AP6] > Host: localhost:4221
[tester::#AP6] >
[tester::#AP6] Sent bytes: "GET /files/banana_mango_blueberry_orange HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 50042) has been established...
[your_program] Request from ('127.0.0.1', 50042):
[your_program] ['GET /files/banana_mango_blueberry_orange HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] headers:  ['Host: localhost:4221']
[tester::#AP6] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 57\r\n\r\npineapple raspberry mango orange orange mango apple grape"
[tester::#AP6] < HTTP/1.1 200 OK
[tester::#AP6] < Content-Type: application/octet-stream
[tester::#AP6] < Content-Length: 57
[tester::#AP6] <
[tester::#AP6] < pineapple raspberry mango orange orange mango apple grape
[tester::#AP6] <
[tester::#AP6] Received response with 200 status code
[tester::#AP6] ✓ Content-Type header is present
[tester::#AP6] ✓ Content-Length header is present
[tester::#AP6] ✓ Body is correct
[your_program] file_path: /tmp/data/codecrafters.io/http-server-tester/banana_mango_blueberry_orange
[your_program] Printing entire response:  b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 57\r\n\r\npineapple raspberry mango orange orange mango apple grape'
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 57\r\n\r\npineapple raspberry mango orange orange mango apple grape'
[tester::#AP6] First test passed.
[tester::#AP6] Testing non existent file returns 404
[tester::#AP6] Connected to localhost port 4221
[tester::#AP6] $ curl -v http://localhost:4221/files/non-existentorange_apple_grape_strawberry
[tester::#AP6] > GET /files/non-existentorange_apple_grape_strawberry HTTP/1.1
[tester::#AP6] > Host: localhost:4221
[tester::#AP6] >
[tester::#AP6] Sent bytes: "GET /files/non-existentorange_apple_grape_strawberry HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 50058) has been established...
[your_program] Request from ('127.0.0.1', 50058):
[your_program] ['GET /files/non-existentorange_apple_grape_strawberry HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] headers:  ['Host: localhost:4221']
[your_program] file_path: /tmp/data/codecrafters.io/http-server-tester/non-existentorange_apple_grape_strawberry
[your_program] Return value of response:  b'HTTP/1.1 404 Not Found\r\n\r\n'
[tester::#AP6] Received bytes: "HTTP/1.1 404 Not Found\r\n\r\n"
[tester::#AP6] < HTTP/1.1 404 Not Found
[tester::#AP6] <
[tester::#AP6] Received response with 404 status code
[tester::#AP6] Test passed.
[tester::#AP6] Terminating program
[tester::#AP6] Program terminated successfully

[tester::#EJ5] Running tests for Stage #EJ5 (Concurrent connections)
[tester::#EJ5] Running program
[tester::#EJ5] $ ./your_server.sh
[tester::#EJ5] Creating 2 parallel connections
[tester::#EJ5] Creating connection 1
[tester::#EJ5] Creating connection 2
[tester::#EJ5] Sending first set of requests
[tester::#EJ5] client-1: $ curl -v http://localhost:4221/
[tester::#EJ5] client-1: > GET / HTTP/1.1
[tester::#EJ5] client-1: > Host: localhost:4221
[tester::#EJ5] client-1: >
[tester::#EJ5] client-1: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 50150) has been established...
[your_program] Connection from ('127.0.0.1', 50152) has been established...Request from ('127.0.0.1', 50150):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] headers:  ['Host: localhost:4221']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-1: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-1: < HTTP/1.1 200 OK
[tester::#EJ5] client-1: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 1
[tester::#EJ5] client-2: $ curl -v http://localhost:4221/
[tester::#EJ5] client-2: > GET / HTTP/1.1
[tester::#EJ5] client-2: > Host: localhost:4221
[tester::#EJ5] client-2: >
[tester::#EJ5] client-2: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program]
[your_program] Request from ('127.0.0.1', 50152):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] headers:  ['Host: localhost:4221']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-2: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-2: < HTTP/1.1 200 OK
[tester::#EJ5] client-2: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 2
[tester::#EJ5] Creating 2 parallel connections
[tester::#EJ5] Creating connection 1
[tester::#EJ5] Creating connection 2
[tester::#EJ5] Sending second set of requests
[tester::#EJ5] client-1: $ curl -v http://localhost:4221/
[tester::#EJ5] client-1: > GET / HTTP/1.1
[tester::#EJ5] client-1: > Host: localhost:4221
[tester::#EJ5] client-1: >
[tester::#EJ5] client-1: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 50158) has been established...
[your_program] Request from ('127.0.0.1', 50158):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] headers:  ['Host: localhost:4221']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-1: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-1: < HTTP/1.1 200 OK
[tester::#EJ5] client-1: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 1
[tester::#EJ5] client-2: $ curl -v http://localhost:4221/
[tester::#EJ5] client-2: > GET / HTTP/1.1
[tester::#EJ5] client-2: > Host: localhost:4221
[tester::#EJ5] client-2: >
[tester::#EJ5] client-2: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 50162) has been established...
[your_program] Request from ('127.0.0.1', 50162):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] headers:  ['Host: localhost:4221']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-2: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-2: < HTTP/1.1 200 OK
[tester::#EJ5] client-2: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 2
[tester::#EJ5] Test passed.
[tester::#EJ5] Terminating program
[tester::#EJ5] Program terminated successfully

[tester::#FS3] Running tests for Stage #FS3 (Read header)
[tester::#FS3] Running program
[tester::#FS3] $ ./your_server.sh
[tester::#FS3] Connected to localhost port 4221
[tester::#FS3] $ curl -v http://localhost:4221/user-agent -H "User-Agent: raspberry/banana-banana"
[tester::#FS3] > GET /user-agent HTTP/1.1
[tester::#FS3] > Host: localhost:4221
[tester::#FS3] > User-Agent: raspberry/banana-banana
[tester::#FS3] >
[tester::#FS3] Sent bytes: "GET /user-agent HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: raspberry/banana-banana\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 50262) has been established...
[your_program] Request from ('127.0.0.1', 50262):
[your_program] ['GET /user-agent HTTP/1.1', 'Host: localhost:4221', 'User-Agent: raspberry/banana-banana', '', '']
[your_program] headers:  ['Host: localhost:4221', 'User-Agent: raspberry/banana-banana']
[tester::#FS3] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: s\r\nContent-Length: a\r\n\r\n"
[tester::#FS3] < HTTP/1.1 200 OK
[tester::#FS3] < Content-Type: s
[tester::#FS3] < Content-Length: a
[tester::#FS3] <
[tester::#FS3] Received response with 200 status code
[your_program] Printing entire response:  b'HTTP/1.1 200 OK\r\nContent-Type: s\r\nContent-Length: a\r\n\r\nr'
[tester::#FS3] Expected "Content-Type" header value to be "text/plain", got "s"
[tester::#FS3] Test failed
[tester::#FS3] Terminating program
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\nContent-Type: s\r\nContent-Length: a\r\n\r\nr'
[tester::#FS3] Program terminated successfully
```

`[tester::#AP6] Expected "Content-Type" header value to be "application/octet-stream", got "application/octet-streamContent-Length: 66"`

# HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 14\r\n\r\nHello, World!

- Correct response

# HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {content_length}\r\n\r\n{content}

```python
response = f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {content_length}\r\n\r\n{content}"
return f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {content_length}\r\n\r\n{content}"
return f"HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}"
return f"HTTP/1.1 {status_code} OK\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n{content}"
```

---

###Running tests for Stage #FS3 (Read header)

⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! FIRST TEST THAT PASSED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳

```bash
jim3@jim3-9020:~/.../codecrafters-http-server-python$ codecrafters test
Initiating test run...

⏳ Turbo test runners busy. You are in queue.

Upgrade to skip the wait: https://codecrafters.io/turbo

Running tests. Logs should appear shortly...

[compile] Compilation successful.

Debug = true

[tester::#AP6] Running tests for Stage #AP6 (Return a file)
[tester::#AP6] Running program
[tester::#AP6] $ ./your_server.sh --directory /tmp/data/codecrafters.io/http-server-tester/
[tester::#AP6] Testing existing file
[tester::#AP6] Creating file orange_apple_blueberry_raspberry in /tmp/data/codecrafters.io/http-server-tester/
[tester::#AP6] File Content: "banana blueberry strawberry orange pineapple pineapple mango blueberry"
[tester::#AP6] Connected to localhost port 4221
[tester::#AP6] $ curl -v http://localhost:4221/files/orange_apple_blueberry_raspberry
[tester::#AP6] > GET /files/orange_apple_blueberry_raspberry HTTP/1.1
[tester::#AP6] > Host: localhost:4221
[tester::#AP6] >
[tester::#AP6] Sent bytes: "GET /files/orange_apple_blueberry_raspberry HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53190) has been established...
[your_program] Request from ('127.0.0.1', 53190):
[your_program] ['GET /files/orange_apple_blueberry_raspberry HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] file_path: /tmp/data/codecrafters.io/http-server-tester/orange_apple_blueberry_raspberry
[your_program] printing contents:  banana blueberry strawberry orange pineapple pineapple mango blueberry
[your_program] Printing bodylen 70
[your_program] Printing entire response:  b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 70\r\n\r\nbanana blueberry strawberry orange pineapple pineapple mango blueberry'
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 70\r\n\r\nbanana blueberry strawberry orange pineapple pineapple mango blueberry'
[tester::#AP6] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 70\r\n\r\nbanana blueberry strawberry orange pineapple pineapple mango blueberry"
[tester::#AP6] < HTTP/1.1 200 OK
[tester::#AP6] < Content-Type: application/octet-stream
[tester::#AP6] < Content-Length: 70
[tester::#AP6] <
[tester::#AP6] < banana blueberry strawberry orange pineapple pineapple mango blueberry
[tester::#AP6] <
[tester::#AP6] Received response with 200 status code
[tester::#AP6] ✓ Content-Type header is present
[tester::#AP6] ✓ Content-Length header is present
[tester::#AP6] ✓ Body is correct
[tester::#AP6] First test passed.
[tester::#AP6] Testing non existent file returns 404
[tester::#AP6] Connected to localhost port 4221
[tester::#AP6] $ curl -v http://localhost:4221/files/non-existentmango_banana_grape_pineapple
[tester::#AP6] > GET /files/non-existentmango_banana_grape_pineapple HTTP/1.1
[tester::#AP6] > Host: localhost:4221
[tester::#AP6] >
[tester::#AP6] Sent bytes: "GET /files/non-existentmango_banana_grape_pineapple HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53206) has been established...
[your_program] Request from ('127.0.0.1', 53206):
[your_program] ['GET /files/non-existentmango_banana_grape_pineapple HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] file_path: /tmp/data/codecrafters.io/http-server-tester/non-existentmango_banana_grape_pineapple
[your_program] Return value of response:  b'HTTP/1.1 404 Not Found\r\n\r\n'
[tester::#AP6] Received bytes: "HTTP/1.1 404 Not Found\r\n\r\n"
[tester::#AP6] < HTTP/1.1 404 Not Found
[tester::#AP6] <
[tester::#AP6] Received response with 404 status code
[tester::#AP6] Test passed.
[tester::#AP6] Terminating program
[tester::#AP6] Program terminated successfully

[tester::#EJ5] Running tests for Stage #EJ5 (Concurrent connections)
[tester::#EJ5] Running program
[tester::#EJ5] $ ./your_server.sh
[tester::#EJ5] Creating 2 parallel connections
[tester::#EJ5] Creating connection 1
[tester::#EJ5] Creating connection 2
[tester::#EJ5] Sending first set of requests
[tester::#EJ5] client-1: $ curl -v http://localhost:4221/
[tester::#EJ5] client-1: > GET / HTTP/1.1
[tester::#EJ5] client-1: > Host: localhost:4221
[tester::#EJ5] client-1: >
[tester::#EJ5] client-1: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[tester::#EJ5] client-1: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53290) has been established...
[your_program] Request from ('127.0.0.1', 53290):
[tester::#EJ5] client-1: < HTTP/1.1 200 OK
[tester::#EJ5] client-1: <
[tester::#EJ5] Received response with 200 status code
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] Closing connection 1
[tester::#EJ5] client-2: $ curl -v http://localhost:4221/
[tester::#EJ5] client-2: > GET / HTTP/1.1
[tester::#EJ5] client-2: > Host: localhost:4221
[tester::#EJ5] client-2: >
[tester::#EJ5] client-2: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53296) has been established...
[your_program] Request from ('127.0.0.1', 53296):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-2: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-2: < HTTP/1.1 200 OK
[tester::#EJ5] client-2: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 2
[tester::#EJ5] Creating 2 parallel connections
[tester::#EJ5] Creating connection 1
[tester::#EJ5] Creating connection 2
[tester::#EJ5] Sending second set of requests
[tester::#EJ5] client-1: $ curl -v http://localhost:4221/
[tester::#EJ5] client-1: > GET / HTTP/1.1
[tester::#EJ5] client-1: > Host: localhost:4221
[tester::#EJ5] client-1: >
[tester::#EJ5] client-1: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53302) has been established...
[your_program] Connection from ('127.0.0.1', 53310) has been established...
[your_program] Request from ('127.0.0.1', 53302):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-1: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-1: < HTTP/1.1 200 OK
[tester::#EJ5] client-1: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 1
[tester::#EJ5] client-2: $ curl -v http://localhost:4221/
[tester::#EJ5] client-2: > GET / HTTP/1.1
[tester::#EJ5] client-2: > Host: localhost:4221
[tester::#EJ5] client-2: >
[tester::#EJ5] client-2: Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Request from ('127.0.0.1', 53310):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#EJ5] client-2: Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#EJ5] client-2: < HTTP/1.1 200 OK
[tester::#EJ5] client-2: <
[tester::#EJ5] Received response with 200 status code
[tester::#EJ5] Closing connection 2
[tester::#EJ5] Test passed.
[tester::#EJ5] Terminating program
[tester::#EJ5] Program terminated successfully

[tester::#FS3] Running tests for Stage #FS3 (Read header)
[tester::#FS3] Running program
[tester::#FS3] $ ./your_server.sh
[tester::#FS3] Connected to localhost port 4221
[tester::#FS3] $ curl -v http://localhost:4221/user-agent -H "User-Agent: blueberry/blueberry-blueberry"
[tester::#FS3] > GET /user-agent HTTP/1.1
[tester::#FS3] > Host: localhost:4221
[tester::#FS3] > User-Agent: blueberry/blueberry-blueberry
[tester::#FS3] >
[tester::#FS3] Sent bytes: "GET /user-agent HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: blueberry/blueberry-blueberry\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53376) has been established...
[tester::#FS3] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: l\r\n\r\n"
[tester::#FS3] < HTTP/1.1 200 OK
[tester::#FS3] < Content-Type: application/octet-stream
[tester::#FS3] < Content-Length: l
[tester::#FS3] <
[tester::#FS3] Received response with 200 status code
[your_program] Request from ('127.0.0.1', 53376):
[your_program] ['GET /user-agent HTTP/1.1', 'Host: localhost:4221', 'User-Agent: blueberry/blueberry-blueberry', '', '']
[tester::#FS3] Expected "Content-Type" header value to be "text/plain", got "application/octet-stream"
[tester::#FS3] Test failed
[tester::#FS3] Terminating program
[your_program] printing contents:  b
[your_program] Printing bodylen l
[your_program] Printing entire response:  b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: l\r\n\r\nb'
[your_program] Return value of response:  b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: l\r\n\r\nb'
[tester::#FS3] Program terminated successfully
```

---

The tester will execute your program with a `--directory` flag. The --directory flag specifies the directory where the files are stored, as an _absolute path_.

`./your_server.sh --directory /tmp/`

The tester will then send two GET requests to the `/files/{filename}` **endpoint** on your server.

### First request

The first request will ask for a file that exists in the files directory:

`echo -n 'Hello, World!' > /tmp/foo`

`curl -i http://localhost:4221/files/foo`

Your server must respond with a `200` response that contains the following parts:

`Content-Type` header set to `application/octet-stream`
`Content-Length` header set to the size of the file, in `bytes`.
`Response` body set to the file _contents_.

```js
HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 14\r\n\r\nHello, World!
```

---

arg.parse info

The return value from `parse_args()` is a Namespace containing the arguments to the command. The object holds the argument values as **attributes**, so if the argument’s
`dest` is set to `"myoption"`, the **value** is accessible as `args.myoption` | or `args.directory`

```py
parser = argparse.ArgumentParser()
parser.add_argument("--directory", type=str)
args = parser.parse_args()
```

---

[tester::#AP6] Running tests for Stage #AP6 (Return a file)
[tester::#AP6] Running program
[tester::#AP6] $ ./your_server.sh --directory /tmp/data/codecrafters.io/http-server-tester/
[tester::#AP6] Testing existing file
[tester::#AP6] Creating file grape_blueberry_blueberry_banana in /tmp/data/codecrafters.io/http-server-tester/
[tester::#AP6] File Content: "blueberry mango pineapple pear banana mango grape blueberry"
[tester::#AP6] Connected to localhost port 4221
[tester::#AP6] $ curl -v http://localhost:4221/files/grape_blueberry_blueberry_banana
[tester::#AP6] > GET /files/grape_blueberry_blueberry_banana HTTP/1.1
[tester::#AP6] > Host: localhost:4221
[tester::#AP6] >
[tester::#AP6] Sent bytes: "GET /files/grape_blueberry_blueberry_banana HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 53264) has been established...
[your_program] Request from ('127.0.0.1', 53264):
[your_program] ['GET /files/grape_blueberry_blueberry_banana HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] list all sub directories: [PosixPath('app'), PosixPath('.git')]
[your_program] Printing entire response: b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 32\r\n\r\ngrape_blueberry_blueberry_banana'
[your_program] Return value of response: b'HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 32\r\n\r\ngrape_blueberry_blueberry_banana'
[tester::#AP6] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: 32\r\n\r\ngrape_blueberry_blueberry_banana"
[tester::#AP6] < HTTP/1.1 200 OK
[tester::#AP6] < Content-Type: application/octet-stream
[tester::#AP6] < Content-Length: 32
[tester::#AP6] <
[tester::#AP6] < grape_blueberry_blueberry_banana
[tester::#AP6] <
[tester::#AP6] Received response with 200 status code
[tester::#AP6] Expected "Content-Length" header value to be "59", got "32"
[tester::#AP6] Test failed
[tester::#AP6] Terminating program
[tester::#AP6] Program terminated successfully

---

possible functions...keep just in case..1

```python
def get_file_name(request_line):
    file = request_line.split()
    if len(file) >= 2 and file[0] == "GET" and file[1].startswith("/files/"):
        # return file[1][len("/files/") :]
        data_part = file[1][len("/files/") :]
        real_data_path = os.path.join("/tmp/data", data_part)
        if os.path.isfile(real_data_path):
            print(real_data_path)
            return real_data_path
        else:
            # Handle the case where the file doesn't exist at the real path
            raise FileNotFoundError(f"Data not found at {real_data_path}")
    return None

```
