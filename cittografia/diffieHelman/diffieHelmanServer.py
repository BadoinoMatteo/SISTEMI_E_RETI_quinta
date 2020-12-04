import socket
import conf

#bob
def main():
    g = conf.g
    N = conf.N
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # creo il server
    server.bind((conf.IP,conf.PORTA))
    server.listen()
    conn,addr=server.accept()
    A=int(conn.recv(conf.BUFFERSIZE).decode())    #ricevo A
    b=int(input("inserisci un numero"))     #chiedo in input b
    B=str(pow(g,b)%N)                     #calcolo B
    conn.sendall(B.encode())                #mando B al client
    keyB=pow(A,b)%N                     #calcolo la chiave B
    print(keyB)




if __name__ == '__main__':
    main()