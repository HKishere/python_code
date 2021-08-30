import serial #导入模块
import threading
import socket  #导入socket模块
import time #导入time模块

PORT = 10002
      # 创建一个套接字socket对象，用于进行通讯
      # socket.AF_INET 指明使用INET地址集，进行网间通讯
      # socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("192.168.1.233", PORT)  
server_socket.bind(address)  # 为服务器绑定一个固定的地址，ip和端口
#server_socket.settimeout(50)  #设置一个时间提示，如果没接到数据进行提示

portx="COM6"
bps=115200
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex=None
ser = serial.Serial(portx,bps,timeout=timex)
print("串口详情参数：", ser)

def UDP2Serial():
      while True:
            msg, client = server_socket.recvfrom(1024)
            print ("%s: %x",client, msg.hex(' '))
            result = ser.write(msg)#写数据
            print("写总字节数:",result)
            ##print(ser.read(125))#读一个字节

if __name__ == '__main__':
      UDP2Serial()
