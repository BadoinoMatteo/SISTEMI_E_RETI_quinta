
def main():
    corr=False
    numA=0
    numB=0
    while corr==False:
        numA = int(input("inserisci primo numero"))
        numB = int(input("inserisci secondo numero"))
        if(numA>numB):
            corr=True
    while numB>0:
        resto=numA%numB
        numA=numB
        numB=resto
    print(f"mcd{numA}")

if __name__ == '__main__':
    main()