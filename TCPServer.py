# 导入 socket、sys 模块
import socket
import sys
import chardet

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = "192.168.2.60"
port = 10002

# 绑定端口号
print(host)
print(port)
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
    
    #msg = clientsocket.recv(1024)
    #print(msg.decode("MBCS"))
    #print(chardet.detect(msg))
    msg_ask = "udp connected!"
    #msg_ask = str(msg_ask)
    clientsocket.send(msg_ask.encode('MBCS'))
    #msg = clientsocket.recv(1024)
    #print(msg.decode("MBCS"))