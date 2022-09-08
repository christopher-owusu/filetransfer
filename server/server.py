import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for any incomming connections.....")
conn, addr = s.accept()
print(addr, "Has connected to server")


filename = input(str("Please enter the filename: "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data transmitted sucessfully.")