import socket
ip='192.168.10.2'
porta='0'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creo il socket
for i in range(0,5000):
	s.bind((ip, porta+1))
	s.listen()  #metto in ascolto il socket
	esitoConn=s.connect_ex()	#connesione con host
	if(esitoConn==0):	#verifica connessione
		print("connessione andata a buon fine")
	else:
		print("connessione fallita")
