import random

n = 4
n2 = n * 2
x = 0
z = 0
e = 0
f = 0
mtr = [list('0' * n) for i in range(n)]

board2 = [list('0' * n) for i in range(n)]

lettere = list('ABCDEFGHILMNOPQRSTUVZ')
random.shuffle(lettere)
random.sample(lettere, n2)
lettere = lettere[:n2] * 2
random.shuffle(lettere)

lettere = [lettere[:4],
           lettere[4:8],
           lettere[8:12],
           lettere[12:16]]
righe = [lettere[:4]]
colonne = [lettere[0]]


#verifica: togliere i commenti per verificare
#print(lettere)
#print('-----------------')
#print(righe)


def generale():
    z = int(input('Scegliere coordinata x,  tra 0 e 3'))
    x = int(input('Scegliere coordinata y tra 0 e 3'))
    e = int(input('Scegliere coordinate x, tra 0 e 3 un altra volta'))
    f = int(input('Scegliere coordinate  y tra 0 e 3 un altra volta'))

    if lettere[e][f] == lettere[z][x]:
        board2[e][f] = lettere[e][f]
    #if lettere[e][f] == lettere[z][x]:
        board2[z][x] = lettere[z][x]
    print(lettere[z][x])
    print(lettere[e][f])
    design()
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    

#Funzione da implementare in futuro
#def inp():
    #e, f = map(int, input('Scegliere coordinate x, y tra 0 e 3'))
    #z, x = map(int, input('Scegliere coordinate x, y tra 0 e 3 un altra volta'))
    #z = int(input('Scegliere coordinata x,  tra 0 e 3'))
   # x = int(input('Scegliere coordinata y tra 0 e 3'))
   # e = int(input('Scegliere coordinate x, tra 0 e 3 un altra volta'))
    #f = int(input('Scegliere coordinate  y tra 0 e 3 un altra volta'))

    print(e, f, x, z)
def finish(val):
    if any('0') in board2:
        return False
    else:
        return True




def design():

    for row in board2:
        print(row)
    print('\n')

def gioca():
    while finish(True):
        design()

    #if validation(True):
        generale()
gioca()
print( 'F   I   N   I   S   H')
