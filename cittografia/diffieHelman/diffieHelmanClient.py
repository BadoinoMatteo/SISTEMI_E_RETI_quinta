import socket
import conf

#alice
def main():
    g=conf.g
    N=conf.N
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #creo il client
    client.connect((conf.IP,conf.PORTA))
    a=int(input("inserisci un numero"))                 #chiedo in input a
    A=str(pow(g,a)%N)                                   #calcolo A
    client.sendall(A.encode())                          #mando A al server
    B=int(client.recv(conf.BUFFERSIZE).decode())        #ricevo B
    keyA=pow(B,a)%N                                     #calcolo la chiave A
    print(keyA)





if __name__ == '__main__':
    main()