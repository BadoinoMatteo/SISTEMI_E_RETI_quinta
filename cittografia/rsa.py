import random

def main():
    p=int(input("inserisci un numero intero primo"))
    q=int(input("inserisci un numero intero primo"))
    n=p*q
    m=mcm(p, q)
    print(m)
    c=trovaC(m)
    print(c)
    d=trovaD(c,m)
    print(d)
    num=int(input("inserisci numero da criptare"))
    criptato=criptaNum(num,c,n)
    print(criptato)
    decriptato=decriptaNum(criptato,d,n)
    print(f"messaggio decifrato={decriptato}")

def mcd(numA, numB):
    if (numA < numB):
        numA, numB = numB, numA
    while numB > 0:
        resto = numA % numB
        numA = numB
        numB = resto
    return numA

def mcm(numA, numB):
    numA-=1
    numB-=1
    return (numA*numB)//mcd(numA, numB)


def trovaC(m):
    lista=[]
    for c in range(2, m):
        if(mcd(c,m)==1):
            lista.append(c)
    print(lista)
    return random.choice(lista)

def trovaD(c,m):
    for d in range(2,m):
        if((c*d)%m==1):
            return d
    return None

def criptaNum(a,c,n):
    return (pow(a,c)%n)

def decriptaNum(b,d,n):
    return (pow(b,d)%n)


if __name__ == '__main__':
    main()