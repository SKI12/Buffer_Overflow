

def j(ai):
	string = ''
	for j in range(1,17):
		if(j<10):
			aj = str(j)
			string = string + hex_str + ai + aj
		elif(j==10):
			aj = 'a'
			string = string + hex_str + ai + aj
		elif(j==11):
			aj = 'b'
			string = string + hex_str + ai + aj
		elif(j==12):
			aj = 'c'
			string = string + hex_str + ai + aj
		elif(j==13):
			aj = 'd'
			string = string + hex_str + ai + aj
		elif(j==14):
			aj = 'e'
			string = string + hex_str + ai + aj
		elif(j==15):
			aj = 'f'
			string = string + hex_str + ai + aj
		elif(j==16):
			aj = '0'
			if ai >= '0' and ai <= '9':
				ai = hex(ord(ai) - 48+ 1).split('x')[1]
			else:
				ai = str(hex(ord(ai) - 97+ 1).split('x')[1])
				if ai == '1':
					ai = 'b'
				elif ai == '2':
					ai = 'c'
				elif ai == '3':
					ai = 'd'
				elif ai == '4':
					ai = 'e'
				elif ai == '5':
					ai = 'f'
				elif ai == '6':
					ai = '0'
			string = string + hex_str + ai + aj
	return string

hex_str = '\\x'
buf = []
for i in range(0,16):
	if(i<10):
		ai = str(i)
		string = j(ai)
	elif(i==10):
		ai = 'a'
		string = j(ai)
	elif(i==11):
		ai = 'b'
		string = j(ai)
	elif(i==12):
		ai = 'c'
		string = j(ai)
	elif(i==13):
		ai = 'd'
		string = j(ai)
	elif(i==14):
		ai = 'e'
		string = j(ai)
	elif(i==15):
		ai = 'f'
		string = j(ai)
	buf.append(string)

for b in buf:
	print b