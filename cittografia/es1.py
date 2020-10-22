def main():
    cifratura()

def cifratura():
    # dizionario alfabeto
    dict = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'L': 9,
        'M': 10,
        'N': 11,
        'O': 12,
        'P': 13,
        'Q': 14,
        'R': 15,
        'S': 16,
        'T': 17,
        'U': 18,
        'V': 19,
        'Z': 20
    }
    #dichiarazione variabili
    chiave="ITIDELPOZZO"
    messaggio="CIAO"
    chiaveCifrata=[]
    messaggioCifrato=[]
    sommaMexChiave= []

    #cifratura chiave
    for c in chiave:
        chiaveCifrata.append(str(dict.get(c)))
    print(chiaveCifrata)

    #cifratura messaggio
    for i in messaggio:
        messaggioCifrato.append(str(dict.get(i)))
    print(messaggioCifrato)

    #somma messaggio e chiave
    for a in range(0,len(messaggioCifrato)):
        sommaMexChiave.append(str(int(chiaveCifrata[a])+ int(messaggioCifrato[a]) % 21))
    print(sommaMexChiave)

if __name__ == '__main__':
    main()