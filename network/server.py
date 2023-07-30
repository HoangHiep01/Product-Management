import socket
from open_brower import open_product_detail

# Định nghĩa host và port mà server sẽ chạy và lắng nghe
host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1) # 1 ở đây có nghĩa chỉ chấp nhận 1 kết nối
print("Server listening on port: ", port)

conn, addr = s.accept()
print("Connect from ", str(addr))

# #server sử dụng kết nối gửi dữ liệu tới client dưới dạng binary
# conn.send(b"Hello, how are you")
# conn.send(b"Bye")

while True:

	message = conn.recv(1024).decode()
	print('Message: ', message)

	if message == 'stop':
		break
	open_product_detail(message)

conn.close()