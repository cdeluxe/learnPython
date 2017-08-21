"""from random import randint as tiRuboLaFunzione

print (tiRuboLaFunzione(0,10))

numero = -5
while numero <= 5:
    print (5/numero)
    numero += 1
"""


numero = -5
while numero <= 5:
    try:
        print (5/numero)
        numero += 1
    except ZeroDivisionError:
        print ('Ops')
        numero += 1
    except:
        print ('Non previsto')
        numero += 1
    finally:
        print('é passato tutto')