#!/usr/bin/python
#coding=utf-8
import socket

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print "\n[*]Sending evil buffer..."
		s.connect(('192.168.220.144', 110))
		data = s.recv(1024)
		print data

		s.send('USER administrator\r\n')
		data = s.recv(1024)
		print data

		s.send('PASS 123456\r\n')
		data = s.recv(1024)
		print data

		s.close()
		print "\n[*]Done!"
	except:
		print "[-]Can't connect to POP3 !"

if __name__ == '__main__':
	main()