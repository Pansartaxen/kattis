cards = input()
go,si,co = cards.split(' ')
go = int(go)
si = int(si)
co = int(co)
victoryCard = 1
if 3*go+2*si+co >= 8:
    victoryCard = 'Province or'
elif 3*go+2*si+co >= 5:
    victoryCard = 'Duchy or'
elif 3*go+2*si+co >= 2:
    victoryCard = 'Estate or'

if 3*go+2*si+co >= 6:
    treasurecard = 'Gold'
elif 3*go+2*si+co >= 3:
    treasurecard = 'Silver'
elif 3*go+2*si+co >= 0:
    treasurecard = 'Copper'
if victoryCard != 1:
    print(f'{victoryCard} {treasurecard}')
else:
    print(f'{treasurecard}')