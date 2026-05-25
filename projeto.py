def Verifique():
    number = int(input("Informe um número inteiro: "))
    
    if number % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
    
    return number  


resultado = Verifique()

print("O número digitado foi:", resultado)
