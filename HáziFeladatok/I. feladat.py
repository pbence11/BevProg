def main():
    print("Adja meg a téglalap oldalait!")
    a=int(input("Add meg az 'a' oldalt: "))
    b=int(input("Add meg a 'b' oldalt: "))
    teglat=a*b
    print("A téglalap területe: ", format(teglat))
    
    pi=3.14
    kors=int(input("Add meg a kör sugarát: "))
    kort=float(kors*kors*pi)
    print("A kör területe: ", format(kort))
    gula=float((kort*teglat)/3)
    print("Gúla térfogata a kapott két értékből: ", format(gula))

if __name__ == "__main__":
    main()