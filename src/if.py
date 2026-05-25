def Verificacao():
    number=int((input("Informe um número inteiro: ")))
    if number % 2 == 0:
        print("O numero", number, "é par")
    else:
        print("O numero", number, "Ímpar")
    return number
resultado = Verificacao()
print("O número digitado foi", resultado)