def main():
    div=[]
    num=int(input("inserisci numero da scomporre"))
    numdiv=2
    if(primo(num)):
        print("numero primo")
    else:
        while num>1:
            if num%numdiv==0:
                num=num/numdiv
                div.append(numdiv)
            else:
                numdiv+=1
        print(div)

def primo(n):
    div, check = 2, 0
    while n / 2 >= div and check == 0:
        if n % div == 0:
            check += 1
        div += 1
    if (check == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    main()