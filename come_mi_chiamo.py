
def domanda1():
    return input ('La tua calcolatrice ha un nome? ' + 'Scegli Si / No: ')
def domanda2():
    return input('Vuoi procedere senza dare un nome alla tua calcolatrice? ' + 'Scegli Si / No: ')
def domanda3():
    return input('Come si chiama la tua calcolatrice? ')

print('Ciao, come ti chiami?')
ilTuoNome = input('Inserisci il tuo nome: ')
ilTuoCognome = input('Inserisci il tuo cognome:')
print('Ciao ' + ilTuoNome + ' ' + ilTuoCognome +  ' è un piacere conoscerti. Io sono una calcolatrice gentile.')

primaRisposta= domanda1()
if primaRisposta == ('Si'):
    domanda3()
elif primaRisposta== ('No'):
    domanda2()
else:
    print('Non ho capito la tua domanda...')
    print('Puoi ripetere gentilmente?')
    domanda1()
    if domanda2() == ('Si'):
        domanda3()
        print ('Ottimo ' + ilTuoNome + ' adesso siamo pronti per iniziare.')
    else:
        cambiatoIdea = input('Non ho capito. ' + 'Hai cambiato idea e vuoi dare un nome alla tua calcolatrice? ' + 'Scegli Si / No ')

        if cambiatoIdea == ('Si'):
            nomeCalcolatrice = input('Come si chiama la tua calcolatrice? ')
