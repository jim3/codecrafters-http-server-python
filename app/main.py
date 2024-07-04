import socket

def main():
	print("Logs from your program will appear here!")
	server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

	while True:
		try:
			conn, client_address = server_socket.accept()
			print(f"Connection from {client_address} has been established.")

			status_line = b"HTTP/1.1 200 OK\r\n\r\n"
			res404 = b"HTTP/1.1 404 Not Found\r\n\r\n"
			
			content_type = b"Content-Type: text/plain\r\n"
			

			recv_data = conn.recv(1024)
			http_request = recv_data.decode('utf-8').splitlines() # -> list[str]
			print("printing http_request: ", http_request)
			
			for i,v in enumerate(http_request):
				print(http_request[i])
				print(len(http_request[i]))

			# request_line = http_request[0]
			# print("printing request_line: ", request_line)

			# for i,v in enumerate(http_request):
			# 	print(i, v)
			# 	print("loop: ", http_request[i])
			
			# for v in request_line:
			# 	split_str = request_line.split(' ') # -> list[str]
			# 	if(split_str[1] != '/'):
			# 		conn.sendall(res404)
			# 	elif(split_str[1] == '/'):
			# 		conn.sendall(status_line)
			# 	else:
			
			# 		None
			

		finally:
			conn.close()
			print(f"Connection from {client_address} has been closed.")

if __name__ == "__main__":
	main
