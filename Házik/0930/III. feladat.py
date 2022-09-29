def main():
    
    szam=(input("Kérlek adj meg egy egész számot!\nSzám: "))
    
    csere=str(szam)
    inverzsz="".join(list(reversed(szam)))
    
    if szam==inverzsz:
        print("A {} tükörszám.". format(szam))
    else:
        print("A {} nem tükörszám.".format(szam))
        
if __name__=="__main__":
    main()