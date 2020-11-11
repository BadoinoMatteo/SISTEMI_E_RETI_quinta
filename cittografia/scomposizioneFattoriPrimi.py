def main():
    div=[]
    num=int(input("inserisci numero da scomporre"))
    numdiv=2
    while num>1:
        print("ok")
        if num%numdiv==0:
            num=num/numdiv
            div.append(numdiv)
        else:
            numdiv+=1
    print(div)



if __name__ == '__main__':
    main()