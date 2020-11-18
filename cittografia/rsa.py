import random

def main():
    p=int(input("inserisci un numero intero"))
    q=int(input("inserisci un numero intero"))
    n=p*q
    m=mcm(p, q)
    print(m)
    c=trovaC(m)
    d=trovaD(c,m)
    num=int(input("inserisci numero da criptare"))
    criptato=criptaNum(num,c,n)
    decriptato=decriptaNum(criptato,d,n)
    print(decriptato)

def mcd(numA, numB):
    if (numA < numB):
        numA, numB = numB, numA
    while numB > 0:
        resto = numA % numB
        numA = numB
        numB = resto
    return numA

def mcm(numA, numB):
    numA-1,numB-1
    return int((numA*numB)/mcd(numA if numA > numB else numB, numA if numA < numB else numB))


def trovaC(m):
    lista=[]
    for c in range(2, m):
        if(mcd(c,m)==1):
            lista.append(c)
    return random.choice(lista)

def trovaD(c,m):
    for d in range(0,m):
        if((c*d)%m==1):
            return d
    return None

def criptaNum(a,c, n):
    return pow(a,c)%n

def decriptaNum(b,d,n):
    return pow(b,d)%n


if __name__ == '__main__':
    main()