
def main():
    numA = int(input("inserisci primo numero"))
    numB = int(input("inserisci primo numero"))
    while numB>0:
        resto=numA%numB
        numA=numB
        numB=resto
    print(numA)
    print(f"mcd{numA}")

if __name__ == '__main__':
    main()