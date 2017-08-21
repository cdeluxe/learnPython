"""
alumni=['Marco','Pietro','Giuseppe']
indice = 0
while indice < 3:
    print (alumni[indice])
    indice += 1
    # += 1 fa sempre "+1"del tipo indicato
    # si puo usare qualsiasi valore
alumni[2] = input ('Chi mettiamo al posto di Giuseppe? ')

alumni=['Marco','Pietro','Giuseppe','Mario']
indice = 0
while indice < len(alumni): #len vuol dire lenght che significa "restituisce la lunghezza"
    print (alumni[indice])
    indice += 1
alumni[2] = input('Chi mettiamo al posto di Giuseppe? ')
alumni.append(input('Chi aggiungo?'))
#append serve per aggiungere qualcosa alla fine della lista
alumni.insert(2,input ('Dimmi un nome: '))
#insert serve per aggiungere qualcosa nella lista dando una posizione specifica
if ('Aldo' in alumni):
    print ('Aldo e nella posizione ' + str(alumni.index('Aldo') + 1))
# +1 dopo alumni.index serve per restituire il numero come contato "dal utente"

print(alumni)

alumni=['Marco','Pietro','Giuseppe','Mario']

for alunno in alumni:
    #for ELEMENTO in LISTA
    print (alunno)
    #stampa tutti i elementi in lista

alumni[2] = input('Chi mettiamo al posto di Giuseppe? ')

alumni.append(input('Chi aggiungo?'))
#append serve per aggiungere qualcosa alla fine della lista

alumni.insert(2,input ('Dimmi un nome: '))
#insert serve per aggiungere qualcosa nella lista dando una posizione specifica

if ('Aldo' in alumni):
    print ('Aldo e nella posizione ' + str(alumni.index('Aldo') + 1))
# +1 dopo alumni.index serve per restituire il numero come contato "dal utente"

print(alumni)
"""

def stampaTutti():
    for alunno in alunni:
        print (alunno)

def sostituisciIndice():
    index = int(input('A quale indice vuoi sostituire? '))
    nome = input('Che nome vuoi dargli? ')
    alunni[index] = nome
    stampaTutti()

def sostituisciNome():
    nomeDaSostituire = input('Quale utente vuoi sostituire? ')
    if (nomeDaSostituire in alunni):
        index = alunni.index(nomeDaSostituire)
        nome = input('Che nome vuoi dargli? ')
        alunni[index] = nome
    else:
        print ('Questo nome non e presente.')
    stampaTutti()

def salva(alunni):
    myfile = open('configurazione.txt', 'w')
    for alunno in alunni:
        myfile.write(alunno + '\n')
    myfile.close()

def carica():
    try:
        myfile = open('configurazione.txt', 'r')
        listaLetta= myfile.readlines()
        listaDaRitornare = []
        for elemento in listaLetta:
            listaDaRitornare.append( elemento.replace('\n',''))

        myfile.close()
        return listaDaRitornare
    except FileNotFoundError:
        print ('Il file non esiste. ')


alunni = ['Marco', 'Pietro', 'Giuseppe', 'Mario']

while True:

    risposta = input ('Cosa vuoi fare? ')
    if risposta == ('stampa'):
        stampaTutti()

    if risposta == ('sostituisci'):
        sostituisciNome()

    if risposta == 'salva':
        salva(alunni)

    if risposta == 'carica':
        alunni = carica()

    if risposta=='esci':
        break
