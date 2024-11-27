from Libro import Catalogodisponibile
from Libro import Catalogonondisponibile
print("Buongiorno, come posso esserle utile? La prego di digitare una delle due opzioni ")
opzioni = int(input("1)vorrei restituire un libro \n2) vorrei prenderne in prestito uno\n "))

if opzioni == 1:
    print("La ringrazio per aver restituito questo libro")
    
else:
    Catalogodisponibile()
    libro = int(input("Inserisci il numero del libro che vorresti prendere, tra questi disponibili: "))
    if libro not in [1,2,3,4,5,6,7,8,9,10]:
        print("Libro non disponibile")
        print("I libri non disponibili sono: ")
        Catalogonondisponibile()
    else:
        print("Grazie per aver preso questo libro")