
def main():
    numA = int(input("inserisci primo numero"))
    numB = int(input("inserisci secondo numero"))
    if(numA<numB):
        numA,numB=numB,numA
    while numB>0:
        resto=numA%numB
        numA=numB
        numB=resto
    print(f"mcd {numA}")

if __name__ == '__main__':
    main()