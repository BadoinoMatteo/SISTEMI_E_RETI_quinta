def main():
    n=int(input("inserisci numero"))
    listaNumPrimi=[]
    contNumPrimi=0
    num=2
    while contNumPrimi<n:
        div, check = 2, 0
        while num/2 >= div and check==0:
            if num % div == 0:
                check+=1
            div+=1
        if(check==0):
            listaNumPrimi.append(num)
            contNumPrimi+=1
        num+=1

    #print(listaNumPrimi)
    print(listaNumPrimi[-1])

if __name__ == '__main__':
    main()