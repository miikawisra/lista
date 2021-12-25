"""Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai
(3)Lopettaa?: 1
Mitä lisätään?: Omenoita
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai
(3)Lopettaa?: 1
Mitä lisätään?: Olutta
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai
(3)Lopettaa?: 2
Listalla on 2 alkiota.
Monesko niistä poistetaan?: 0
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai
(3)Lopettaa?: 3
Listalla oli tuotteet:
Olutta"""

lista= []
jatkuu = True
while jatkuu:
    eka = int(input("""Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?:"""))
    if eka == 1:
        toka = (input("Mitä lisätään?:"))
        lista.append(toka)
    elif eka == 2:
        try:
            print("Listalla on ", len(lista), " alkiota.")
            kolme = int(input("Monesko niistä poistetaan?:"))
            lista.pop(kolme)
        except:
            print("Virheellinen valinta.")
    elif eka == 3:
        print("Listalla oli tuotteet:")
        for i in lista:
            print(i)
        exit()
    else:
        print("Virheellinen valinta.")
