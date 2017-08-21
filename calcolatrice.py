

"""
    def altroNumero():
        altroNumero = input('Vuoi inserire un altro numero? ' + 'Scegli: Si / No ')
        if altroNumero == ('Si'):
            num3 = int(input('Inserisci un altro numero: '))
            print ('Il risultato è: = + str(num1 + num2 + num3'))

        else:

"""
while True:


    comand = input('Scegli tra le seguenti operazioni: + , - , * , / : ')

    if  comand == '+':
        num1 = int(input('Inserisci il primo numero: '))
        num2 = int(input('Inserisci il secondo numero: '))
        print("il risultato è: " + str(num1 + num2))

    elif comand == '-':
        num1 = int(input('Inserisci il primo numero: '))
        num2 = int(input('Inserisci il secondo numero: '))
        print("il risultato è: " + str(num1 - num2))

    elif comand == '*':
        num1 = int(input('Inserisci il primo numero: '))
        num2 = int(input('Inserisci il secondo numero: '))
        print("il risultato è: " + str(num1 * num2))

    elif comand == '/':
        num1 = int(input('Inserisci il primo numero: '))
        num2 = int(input('Inserisci il secondo numero: '))
        print("il risultato è: " + str(num1 / num2))

    elif comand == "quit":
        break
