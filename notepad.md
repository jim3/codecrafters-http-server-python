> Read Header Challenging Passed Test Output

```bash
Initiating test run...

⚡ This is a turbo test run. https://codecrafters.io/turbo

Running tests. Logs should appear shortly...

Debug = true

### [tester::#FS3] Running tests for Stage #FS3 (Read header)
[tester::#FS3] Running program
[tester::#FS3] $ ./your_server.sh
[your_program] Server is listening on port 4221...
[tester::#FS3] Connected to localhost port 4221
[tester::#FS3] $ curl -v http://localhost:4221/user-agent -H "User-Agent: pear/mango-blueberry"
[tester::#FS3] > GET /user-agent HTTP/1.1
[tester::#FS3] > Host: localhost:4221
[tester::#FS3] > User-Agent: pear/mango-blueberry
[tester::#FS3] >
[tester::#FS3] Sent bytes: "GET /user-agent HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: pear/mango-blueberry\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 39606) has been established.
[your_program] Connection from ('127.0.0.1', 39606) has been established...
[your_program] Request from ('127.0.0.1', 39606):
[your_program] ['GET /user-agent HTTP/1.1', 'Host: localhost:4221', 'User-Agent: pear/mango-blueberry', '', '']
[your_program] request_line:  GET /user-agent HTTP/1.1
[your_program] headers:  ['Host: localhost:4221', 'User-Agent: pear/mango-blueberry']
[your_program] response_body:  User-Agent: pear/mango-blueberry
[your_program] User-Agent: pear/mango-blueberry
[your_program] return value of response:  b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 20\r\n\r\npear/mango-blueberry'
[tester::#FS3] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 20\r\n\r\npear/mango-blueberry"
[tester::#FS3] < HTTP/1.1 200 OK
[tester::#FS3] < Content-Type: text/plain
[tester::#FS3] < Content-Length: 20
[tester::#FS3] <
[tester::#FS3] < pear/mango-blueberry
[tester::#FS3] <
[tester::#FS3] Received response with 200 status code
[tester::#FS3] ✓ Content-Type header is present
[tester::#FS3] ✓ Content-Length header is present
[tester::#FS3] ✓ Body is correct
[tester::#FS3] Test passed.
[tester::#FS3] Terminating program
[tester::#FS3] Program terminated successfully

## [tester::#CN2] Running tests for Stage #CN2 (Respond with body)
[tester::#CN2] Running program
[tester::#CN2] $ ./your_server.sh
[your_program] Server is listening on port 4221...
[tester::#CN2] Connected to localhost port 4221
[tester::#CN2] $ curl -v http://localhost:4221/echo/banana
[tester::#CN2] > GET /echo/banana HTTP/1.1
[tester::#CN2] > Host: localhost:4221
[tester::#CN2] >
[tester::#CN2] Sent bytes: "GET /echo/banana HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 39702) has been established.
[your_program] Connection from ('127.0.0.1', 39702) has been established...
[your_program] Request from ('127.0.0.1', 39702):
[your_program] ['GET /echo/banana HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] request_line:  GET /echo/banana HTTP/1.1
[your_program] headers:  ['Host: localhost:4221']
[your_program] response_body:
[your_program] Echo string found: banana
[your_program] return value of response:  b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\n\r\nbanana'
[tester::#CN2] Received bytes: "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\n\r\nbanana"
[tester::#CN2] < HTTP/1.1 200 OK
[tester::#CN2] < Content-Type: text/plain
[tester::#CN2] < Content-Length: 6
[tester::#CN2] <
[tester::#CN2] < banana
[tester::#CN2] <
[tester::#CN2] Received response with 200 status code
[tester::#CN2] ✓ Content-Type header is present
[tester::#CN2] ✓ Content-Length header is present
[tester::#CN2] ✓ Body is correct
[tester::#CN2] Test passed.
[tester::#CN2] Terminating program
[tester::#CN2] Program terminated successfully

## [tester::#IH0] Running tests for Stage #IH0 (Extract URL path)
[tester::#IH0] Running program
[tester::#IH0] $ ./your_server.sh
[your_program] Server is listening on port 4221...
[tester::#IH0] Connected to localhost port 4221
[tester::#IH0] $ curl -v http://localhost:4221/mango
[tester::#IH0] > GET /mango HTTP/1.1
[tester::#IH0] > Host: localhost:4221
[tester::#IH0] >
[tester::#IH0] Sent bytes: "GET /mango HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[tester::#IH0] Received bytes: "HTTP/1.1 404 Not Found\r\n\r\n"
[tester::#IH0] < HTTP/1.1 404 Not Found
[tester::#IH0] <
[your_program] Connection from ('127.0.0.1', 39786) has been established.
[your_program] Connection from ('127.0.0.1', 39786) has been established...
[tester::#IH0] Received response with 404 status code
[your_program] Request from ('127.0.0.1', 39786):
[your_program] ['GET /mango HTTP/1.1', 'Host: localhost:4221', '', '']
[tester::#IH0] Test passed.
[tester::#IH0] Terminating program
[your_program] request_line:  GET /mango HTTP/1.1
[your_program] headers:  ['Host: localhost:4221']
[your_program] response_body:
[your_program] return value of response:  b'HTTP/1.1 404 Not Found\r\n\r\n'
[tester::#IH0] Program terminated successfully

## [tester::#IA4] Running tests for Stage #IA4 (Respond with 200)
[tester::#IA4] Running program
[tester::#IA4] $ ./your_server.sh
[your_program] Server is listening on port 4221...
[tester::#IA4] Connected to localhost port 4221
[tester::#IA4] $ curl -v http://localhost:4221/
[tester::#IA4] > GET / HTTP/1.1
[tester::#IA4] > Host: localhost:4221
[tester::#IA4] >
[tester::#IA4] Sent bytes: "GET / HTTP/1.1\r\nHost: localhost:4221\r\n\r\n"
[your_program] Connection from ('127.0.0.1', 39884) has been established.
[your_program] Connection from ('127.0.0.1', 39884) has been established...
[your_program] Request from ('127.0.0.1', 39884):
[your_program] ['GET / HTTP/1.1', 'Host: localhost:4221', '', '']
[your_program] request_line:  GET / HTTP/1.1
[your_program] headers:  ['Host: localhost:4221']
[your_program] response_body:
[your_program] return value of response:  b'HTTP/1.1 200 OK\r\n\r\n'
[tester::#IA4] Received bytes: "HTTP/1.1 200 OK\r\n\r\n"
[tester::#IA4] < HTTP/1.1 200 OK
[tester::#IA4] <
[tester::#IA4] Received response with 200 status code
[tester::#IA4] Test passed.
[tester::#IA4] Terminating program
[tester::#IA4] Program terminated successfully

## [tester::#AT4] Running tests for Stage #AT4 (Bind to a port)
[tester::#AT4] Running program
[tester::#AT4] $ ./your_server.sh
[tester::#AT4] Connecting to localhost:4221 using TCP
[your_program] Server is listening on port 4221...
[tester::#AT4] Success! Closing connection
[tester::#AT4] Test passed.
[tester::#AT4] Terminating program
[tester::#AT4] Program terminated successfully

All tests passed. Congrats!

Submit your changes to move to the next step:

$ codecrafters submit
```
