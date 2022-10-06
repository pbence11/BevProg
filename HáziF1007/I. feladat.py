"""## II. feladat
Implementálj 3 tetszőleges matematikai képletet!
pl.: pitagorasz-tétel, sinus/cosinus/tangens háromszögben, másodfukú egyenlet megoldóképlet"""

import telnetlib

def decodC():
    
    decodtext = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    emptyT =""
    
    for i in range(len(decodtext)):
        decoding = ord(decodtext[i])
        emptyT += chr(decoding - 3)
        
    print("***Az eredeti szöveg***\n {0}\n\n***Dekódolt szöveg***\n {1}".format(decodtext,emptyT))
    
def main():
    decodC()

if __name__=="__main__":
    main()